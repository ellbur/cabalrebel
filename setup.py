#!/usr/bin/env python

from setuptools import setup

setup(
    name       = 'cabalrebel',
    version    = '0.123',
    py_modules = ['cabalrebel'],
    install_requires = ['scooter>=2'],
    dependency_links = [
        'https://github.com/ellbur/scooter/archive/master.zip#scooter-2'
    ]
)

