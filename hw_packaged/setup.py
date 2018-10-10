from distutils.core import setup
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__),
                             fname)).read()

setup(
    name='Knapsacking',
    version='0.1',
    description='Packaged version of code for solving knapsack problem',
    author='Boguslav Pozniak',
    author_email='boguslav_pozniak@epam.com',
    url='http://www.epam.com',
    scripts=['start_app.py', ],
    packages=['package', ],
    long_description=read('README'),
)
