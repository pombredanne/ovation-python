# Ovation Python API


Ovation is the powerful data management service engineered specifically for scientists that liberates research through organization of multiple data formats and sources, the ability to link raw data with analysis and the freedom to safely share all of this with colleagues and collaborators.

The Ovation Python API wraps the Ovation Java API for use by CPython. Through this Python API, CPython users can access the full functionality of the Ovation ecosystem from within Python. 

Jython users can access the Ovation Java API directly and should *not* use this Python API.


## Requirements

* Java 1.6+
* CPython 2.7+ or 3.3+
* NumPy 1.7+
* Quantities 0.10+

## Building

To build the python wrapper at the command line:

	mvn clean compile

Build requires:

* Java 1.6 or later
* Maven 3 or later
* CPython 2.7 or later

## Installation

Download the ovation-python `egg` from http://ovation.io. Install the `egg` with `easy_install`. At the command line::

	$ sudo easy_install ovation-python-[PY_VERSION]-[OS].egg
	
where `PY_VERSION` is your Python version and `OS` is your operating system. 

.. warning::
	[OS X python + keychain]

## Usage


### Connecting to the Ovation database

	>> from ovation import *
	>> from ovation.connection import connect
	>> dsc = connect(<ovation.io user email>)
	Ovation password: <ovation.io password>
	>> context = dsc.getContext()
	




