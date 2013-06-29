#!/usr/bin/env python

import os.path

from setuptools import setup

# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
    
VERSION = "2.0-beta1"
setup(name='ovation-api',
      version=VERSION,
      description='Low-level Ovation API wrapper module',
      author='Physion',
      author_email='info@ovation.io',
      url='http://ovation.io',
      long_description=read('README.md'),
      classifiers=[
          "Development Status :: 4 - Beta",
          "Intended Audience :: Science/Research",
          "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
      ],
      install_requires=["jcc >= 2.16"]
)
