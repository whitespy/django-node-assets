from setuptools import setup, find_packages


setup(
    name='django-node-assets',
    version='0.9.12',
    description='The Django application that allows install and serve assets via Node.js package '
    'manager infrastructure.',
    author='Andrey Butenko',
    author_email='whitespysoftware@gmail.ru',
    url='https://github.com/whitespy/django-node-assets',
    long_description=open('README.rst', encoding='utf-8').read(),
    packages=find_packages(),
    include_package_data=True,
    keywords='django assets staticfiles Node.js npm package.json',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
        'Framework :: Django :: 4.1',
    ],
)
