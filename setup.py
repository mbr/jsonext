#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='jsonext',
    version='0.1dev',
    description='Well-structured helpers to help serializing commonly '
                'encountered structures to JSON (like datetime, to_dict(), '
                ' etc.',
    long_description=read('README.rst'),
    author='Marc Brinkmann',
    author_email='git@marcbrinkmann.de',
    url='http://github.com/mbr/jsonext',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    install_requires=['times'],
)
