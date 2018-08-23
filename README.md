# Pylint import issue demo
## Issue description

This repo contains a working demonstration for a bug in Pylint regarding the
way it handles imports. An import that's perfectly valid as far as Python's
concerned throws a false positive when checked by Pylint.

The reason is that the top-level folder is named the same as the first
subfolder and contains an `__init__.py`. This turns it into a module, and
despite the fact that `PYTHONPATH` points to this folder (which would imply
only its subfolders are considered as modules), it somehow confuses this
as the module refered to by the name `myproject`.

There are two ways to make pylint pass:

1. Remove the top level `__init__.py`
2. Rename the top-level `myproject` folder

The second approach keeps the `__init__.py` intact, but allows Pylint to lint
the file without import errors. This would indicate that Pylint considers both
the parent folder of the top-level `myproject`, as well as the top-level
`myproject` folder itself as valid module paths. The former is inconsistent
with how Python sees things.

## How to run

The `run_test` script in the root of this repo contains a script that
demonstrates the bug:

1. It starts by creating a virtualenv named `myproject` in which to install Pylint
   If it already exists, it is merely activated.
2. It then sets `PYTHONPATH` to the current working directory.
3. Next, it installs Pylint if necessary.
4. Then it runs the script, to demonstrate that it's valid Python.
5. After which it runs Pylint to show the invalid linter error w.r.t. the import.
6. Then it removes the top-level `__init__.py` and runs Pylint again. The error is gone.
7. Finally, it reinstates the top-level `__init__.py` so the script can run again.

## Prerequisites

The script requires virtualenvwrapper to be installed. It tries to load the
virtualenvwrapper.sh file which defines things like `workon` and `mkvirtualenv`
by finding its location through dpkg. So it assumes a Debian system. When
running on a non-Debian system, simply change the `source` line in the script
to point to the correct path instead.
