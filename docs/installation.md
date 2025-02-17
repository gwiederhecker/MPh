﻿Installation
------------

MPh is [available on PyPI][dist] and can be readily installed via `pip`:
```none
pip install mph
```
Run `pip uninstall mph` in order to remove the library from your system.

Requires [JPype][jpype] for the bridge from Python to [Comsol's
Java API][japi] and [NumPy][numpy] for returning (fast) numerical arrays.
`pip` makes sure the two Python dependencies are installed and adds them
if missing.

Comsol, obviously, you need to license and install yourself. Versions
from Comsol 5.1 onward are expected to work. If you want to use the
client–server mode, make sure to once run `comsolmphserver` from a
console first to enter the obligatory user name and password.

Support for Linux and macOS is limited: Stand-alone clients do not work
out of the box. (As opposed to running client–server mode, which does.)
You have to, once and for all, configure your shell's environment to
work around this issue. Find more details in the chapter
[Limitations](limitations).

Note how a separate Java run-time environment is *not* required, as
Comsol ships with one already built in.


[dist]:  https://pypi.python.org/pypi/mph
[jpype]: https://jpype.readthedocs.io
[japi]:  https://comsol.com/documentation/COMSOL_ProgrammingReferenceManual.pdf
[numpy]: https://numpy.org
