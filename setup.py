from setuptools import setup, find_packages


setup(
    name='django-node-assets',
    version='0.9.2',
    description='The Django application that allows install and serve assets via Node.js package '
                'manager infrastructure.',
    author='Andrey Butenko',
    author_email='whitespysoftware@yandex.ru',
    url='https://github.com/whitespy/django-node-assets',
    long_description=open('README.rst').read(),
    packages=find_packages(),
    include_package_data=True,
    keywords='django assets staticfiles Node.js npm'
)
