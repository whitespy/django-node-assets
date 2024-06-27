#########
Changelog
#########

Release 0.9.14
--------------

- Added the NODE_PACKAGE_MANAGER_INSTALL_OPTIONS setting
- Declared compatibility with Python 3.12 and Django 5.0
- Removed Django 3.2/4.1 versions support

Release 0.9.13
--------------

- Moved package configuration to pyproject.toml
- Added feature to get path to npm executable automatically by using shutil.which function, thanks to `prplecake <https://github.com/prplecake>`_
- Declared compatibility with Django 4.2

Release 0.9.12
--------------

- Fixed a typo in README.rst, thanks to `proofit404 <https://github.com/proofit404>`_
- Declared compatibility with Python 3.11 and Django 4.1

Release 0.9.11
--------------

- Reformatted code with Black
- Replaced subprocess.Popen by subprocess.check_output method to call npm install command
- Replaced os, os.path, shutil module features by pathlib module features
- Remove Python3.6 and Django 2.1/3.0/3.1 versions support, add Django 4.0 support

Release 0.9.10
--------------

- Declared compatibility with Python 3.10

Release 0.9.9
-------------

- Sorted imports by isort
- Updated documentation

Release 0.9.8
-------------

- Dropped Python 3.4, Python 3.5 and Django 2.0 support
- Declared compatibility with Python 3.9 and Django 3.1

Release 0.9.7
-------------

- Fixed package.json copying

Release 0.9.6
-------------

- Added __init__.py files to management and management/commands directories to build distributive properly (issue https://github.com/pypa/setuptools/issues/97)

Release 0.9.5
-------------

- Stopped using symbolic link to copy package.json (issue https://github.com/whitespy/django-node-assets/issues/2)

Release 0.9.4
-------------

- Fixed NodeModulesFinder.find method

Release 0.9.3
-------------

- Improved the npminstall management command
- Changed imports order

Release 0.9.2
-------------

- Updated README.rst

Release 0.9.1
-------------

- Supplemented README.rst

Release 0.9.0
-------------

- Initial release
