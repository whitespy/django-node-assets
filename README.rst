##################
Django-node-assets
##################

.. image:: https://badge.fury.io/py/django-node-assets.svg
    :target: https://badge.fury.io/py/django-node-assets

.. image:: https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336
    :target: https://pycqa.github.io/isort/

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

.. image:: https://github.com/whitespy/django-node-assets/actions/workflows/code_quality_check.yml/badge.svg
    :target: https://github.com/whitespy/django-node-assets/actions/workflows/code_quality_check.yml

|

The Django application that allows to install and to serve static assets via Node.js package manager infrastructure.
The application exposes management command to install dependencies from your **package.json** and several static files
finders to find files from installed node packages and exclude metadata of node packages and unwanted files when
static files will be collected via Django`s **collectstatic** management command execution.

Features
--------

- Avoiding vendoring static assets in your repository like jQuery plugins, Bootstrap toolkit, etc
- Avoiding mess in **STATIC_ROOT** through exclusion node packages` metatadata and unwanted files
- Installing dependencies by Django`s management command

Installation
------------

.. code:: bash

    $ pip install django-node-assets

Configuration
-------------

Add 'django_node_assets' to your INSTALLED_APPS:

.. code:: python

    INSTALLED_APPS = [
        ...
        'django_node_assets',
    ]

Add NodeModulesFinder to STATICFILES_FINDERS:

.. code:: python

    STATICFILES_FINDERS = [
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        'django_node_assets.finders.NodeModulesFinder',
    ]

Specify absolute path to the package.json file:

.. code:: python

    NODE_PACKAGE_JSON = '/var/assets/package.json'

.. note::

    A package.json must have the "dependencies" section and look like:

    .. code:: json

        {
            "dependencies": {
                "jquery": "^3.2.1",
                "bootstrap": "^3.3.5",
            }
        }

    Details here: https://docs.npmjs.com/files/package.json#dependencies


Specify the absolute path to a directory where the **npminstall** management command will install assets:

.. code:: python

    NODE_MODULES_ROOT = '/var/assets/node_modules'

.. note::

    A base dir must be called **node_modules**.

Override path to the node package manager executable (optional)

.. code:: python

    NODE_PACKAGE_MANAGER_EXECUTABLE = '/usr/local/bin/npm'

.. note::

    The node package manager must be already installed in your system.

Override options of the node package manager install command (optional)

.. code:: python

    NODE_PACKAGE_MANAGER_INSTALL_OPTIONS = ['--dry-run']

Defaults to **--no-package-lock**, **--production**.

Usage
-----

Call the **npminstall** management command to install dependencies specified in the package.json

.. code:: bash

    $ python manage.py npminstall

Use Django`s static template tag to link installed assets

.. code:: html

    {% load static %}

    <link rel="stylesheet" type="text/css" href="{% static 'bootstrap/dist/css/bootstrap.min.css' %}">
    <!-- Some amazing markup -->
    <script src="{% static 'jquery/dist/jquery.min.js' %}"></script>
    <script src="{% static 'bootstrap/dist/js/bootstrap.js' %}"></script>
