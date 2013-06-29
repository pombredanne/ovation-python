#!/usr/bin/env python

import os.path

from setuptools import setup

# Utility function to read the README file.
def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return "Ovation Python API"
    
VERSION = "2.0-beta1"
setup(name='ovation',
      version=VERSION,
      description='Ovation Python API',
      author='Physion',
      author_email='info@ovation.io',
      url='http://ovation.io',
      long_description=read('README.md'),
      packages=['ovation', 'ovation.api', 'ovation.core', 'ovation.test', 'ovation.test.util'],
      classifiers=[
          "Development Status :: 4 - Beta",
          "Intended Audience :: Science/Research",
          "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
      ],
      setup_requires=['nose>=1.3.0', 'coverage==3.6'],
      install_requires=["ovation-api == {version}".format(version=VERSION),
                        "scipy >= 0.12.0",
                        "numpy >= 1.7.1",
                        "pandas >= 0.11.0",
                        "quantities >= 0.10.1",
                        ],
)
