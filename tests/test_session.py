﻿"""Tests a local Comsol session."""
__license__ = 'MIT'


########################################
# Dependencies                         #
########################################
import parent
import mph
import logging
from sys import argv
from pathlib import Path


########################################
# Fixtures                             #
########################################
client = None
cores  = 1
model  = None
here   = Path(__file__).parent
file   = here/'capacitor.mph'


def setup_module():
    pass


def teardown_module():
    pass


########################################
# Tests                                #
########################################


def test_init():
    global client
    client = mph.start(cores=cores)
    assert client.java is not None
    assert not client.models()
    assert client.cores == cores


def test_load():
    global model
    assert file.is_file()
    model = client.load(file)
    assert model


def test_caching():
    assert not client.caching()
    copy = client.load(file)
    assert model != copy
    client.remove(copy)
    client.caching(True)
    assert client.caching()
    copy = client.load(file)
    assert model == copy
    client.caching(False)
    assert not client.caching()


def test_create():
    name = 'test'
    client.create(name)
    assert name in client.names()


def test_models():
    pass


def test_names():
    assert model.name() in client.names()


def test_files():
    assert file.resolve() in client.files()


def test_remove():
    name = model.name()
    client.remove(model)
    assert name not in client.names()
    message = ''
    try:
        model.java.component()
    except Exception as error:
        message = error.getMessage()
    if client.port:
        assert 'no_longer_in_the_model' in message
    else:
        assert 'is_removed' in message


def test_clear():
    client.clear()
    assert not client.models()


def test_disconnect():
    if client.port:
        client.disconnect()
        try:
            client.models()
            connected = True
        except Exception:
            connected = False
        assert not connected


########################################
# Main                                 #
########################################

if __name__ == '__main__':

    arguments = argv[1:]
    if 'stand-alone' in arguments:
        mph.config.option('session', 'stand-alone')
    if 'client-server' in arguments:
        mph.config.option('session', 'client-server')
    if 'log' in arguments:
        logging.basicConfig(
            level   = logging.DEBUG if 'debug' in arguments else logging.INFO,
            format  = '[%(asctime)s.%(msecs)03d] %(message)s',
            datefmt = '%H:%M:%S')

    setup_module()
    try:
        test_init()
        test_load()
        test_caching()
        test_create()
        test_models()
        test_names()
        test_files()
        test_remove()
        test_clear()
        test_disconnect()
    finally:
        teardown_module()
