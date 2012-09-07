#!/usr/bin/env python

import os
from sys import version_info
from setuptools import setup

fp = open(os.path.join(os.path.dirname(__file__), "README.rst"))
readme_text = fp.read()
fp.close()

DESCRIPTION = 'Utility library to help development of RIA on top of a Django backend'

setup(
    name='django-js-utils',
    author='Vebjorn Ljosa',
    author_email='vebjorn@ljosa.com',
    packages=['django_js_utils'],
    version='0.0.5dev',
    description=DESCRIPTION,
    long_description=readme_text,
    install_requires=['django'],
    package_data={
        'django_js_utils': ['static/django_js_utils.js'],
    },
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities'
    ]
)
