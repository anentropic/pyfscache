#!/usr/bin/env python

import os

from ConfigParser import ConfigParser
from setuptools import setup, find_packages


config = ConfigParser()
config.read('PackageInfo.cfg')
info = dict(config.items('main'))

setup(
    name=info['package'],
    version="%(major)s.%(minor)s.%(micro)s%(tag)s" % info,
    author=info['author'],
    author_email=info['email'],
    url=info['url'],
    description=info['description'],
    license=info['license'],
    long_description=open('README.rst').read(),
    packages=find_packages(),
    package_data={'': [os.path.join('*', '*.*')]},
    include_package_data=True,
    # requires=[],
    test_suite=info['package'] + '.tests.test_suite',
    classifiers=[
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
)
