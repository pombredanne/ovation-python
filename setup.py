#!/usr/bin/env python

from setuptools import setup

VERSION = "2.0-SNAPSHOT"
setup(name='Ovation',
      version=VERSION,
      description='Ovation Python API',
      author='Physion',
      author_email='info@ovation.io',
      url='http://ovation.io',
      packages=['ovation'],
      #install_requires=["ovation_api >= {version}".format(version=VERSION)]
     )