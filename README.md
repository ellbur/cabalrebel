
`cabalrebel` is a tool to build Haskell cabal packages using Python `setuptools`.

`cabalrebel` provides the following behavior:

1. synthesizes `*.cabal` and `Setup.hs` files.

2. Invokes `runghc` on `Setup.hs`

How to use it
-------------

Create a `setup.py` file like the following:

    #!/usr/bin/env python
    
    from setuptools import setup
    from setuptools.command.install import install as default_install
    
    class Install(default_install):
        def run(self):
            default_install.do_egg_install(self)
            
            from cabalrebel import cabal_install
            
            cabal_install(
                name = 'joes-house',
                license = 'BSD3',
                author = 'Joe',
                maintainer = 'joe@gmail.com',
                category = '',
                modules = ['Joe.House']
            )
    
    setup(
        name       = 'joes-house',
        version    = '0.123',
        install_requires = ['cabalrebel'],
        dependency_links = [
            'https://github.com/ellbur/cabalrebel/archive/master.zip#cabalrebel-0.123'
        ],
        
        cmdclass = {
            'install' : Install
        }
    )

You will also need to have a `LICENSE` file because `cabal` requires it.

Then run as you would normally for Python:

    python setup.py install

And that should build and install your Haskell module.

