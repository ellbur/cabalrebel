#!/usr/bin/env python

from setuptools import setup
from setuptools.command.install import install as default_install

class Install(default_install):
    def run(self):
        default_install.do_egg_install(self)

        from cabalrebel import cabal_install

        cabal_install(
            name = 'cabalrebel-basic-demo',
            license = 'BSD3',
            author = 'Owen',
            maintainer = 'ellbur@gmail.com',
            category = '',
            modules = ['CabalRebel.BasicDemo']
        )

setup(
    name       = 'haskell-hangul',
    version    = '0.123',
    install_requires = ['cabalrebel'],
    dependency_links = [
        'https://github.com/ellbur/cabalrebel/archive/master.zip#cabalrebel-0.123'
    ],

    cmdclass = {
        'install' : Install
    }
)

