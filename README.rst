##################
Django-node-assets
##################

The Django application that allows install and serve assets via Node.js package manager infrastructure.

Installation
------------

.. code:: bash

    $ pip install django-node-assets

Configuration
-------------

1. Add 'django_node_assets' to your INSTALLED_APPS:

.. code:: python

    INSTALLED_APPS = [
        ...
        'django_node_assets',
    ]

2. Add NodeModulesFinder or ManifestNodeModulesFinder to STATICFILES_FINDERS:

.. code:: python

    STATICFILES_FINDERS = [
        ...
        'django_node_assets.finders.ManifestNodeModulesFinder',
    ]

3. Specify absolute path to the package.json file:

.. code:: python

    NODE_PACKAGE_JSON = '/home/www/projects/foo/requirements/package.json'

4. Specify the absolute path to a directory where the **nmpinstall** management command will install assets:

.. code:: python

    NODE_MODULES_ROOT = '/home/www/assets/foo/node_modules'

5. Specify path to the nmp executable file (optional /usr/bin/npm by default):

.. code:: python

    NODE_PACKAGE_MANAGER_EXECUTABLE = '/usr/local/bin/npm'
