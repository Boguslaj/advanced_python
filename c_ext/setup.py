from distutils.core import Extension
from distutils.core import setup


if __name__ == '__main__':
    setup(name='fibModule',
          version='2.0',
          ext_modules=[Extension('fibModule', ['fib.c'])]
          )
