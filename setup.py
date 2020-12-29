#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

from django_actual import settings

import os

here = os.path.dirname(os.path.abspath(__file__))
f = open(os.path.join(here, 'README.rst'))
long_description = f.read().strip()
where = os.path.join(here, 'README.rst')
f.close()

setup(
    name='django-actual-helpers',
    version=settings.VERSION,
    author='Sipmann',
    author_email='mauricio@sipmann.com',
    url='http://github.com/sipmann/django-actual-helpers',
    description='Common things every Django app needs Based on django-common-helpers package',
    packages=find_packages(),
    long_description=long_description,
    keywords=['django', 'scaffold'],
    zip_safe=False,
    install_requires=[
        'Django>=3.1.4'
    ],
    python_requires='>=3',
    test_suite='django_actual.tests',
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Development Status :: 4 - Beta',
        "Programming Language :: Python :: 3",
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
