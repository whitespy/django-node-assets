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

2. Add NodeModulesFinder to STATICFILES_FINDERS:

.. code:: python

    STATICFILES_FINDERS = [
        ...
        'django_node_assets.finders.NodeModulesFinder',
    ]

3. Specify absolute path to the package.json file:

.. code:: python

    NODE_PACKAGE_JSON = '/var/assets/package.json'

.. note::

    A package.json must have the "dependencies" section and look like:

    .. code:: json

        {
            "dependencies": {
                "jquery": "^3.2.1",
                "jquery-migrate": "^3.0.0",
            }
        }

    Details here: https://docs.npmjs.com/files/package.json#dependencies


4. Specify the absolute path to a directory where the **nmpinstall** management command will install assets:

.. code:: python

    NODE_MODULES_ROOT = '/var/assets/node_modules'

.. note::

    A base dir must be called **node_modules**.

5. Specify path to the nmp executable (optional)

.. code:: python

    NODE_PACKAGE_MANAGER_EXECUTABLE = '/usr/local/bin/npm'

.. note::

    The Node.js package manager must be already installed in your system.

Usage
-----

Call the **nmpinstall** management command to install assets specified in the package.json

.. code:: bash

    $ python manage.py npminstall
