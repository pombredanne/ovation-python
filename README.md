# Ovation Python API


Ovation is the powerful data management service engineered specifically for scientists that liberates research through organization of multiple data formats and sources, the ability to link raw data with analysis and the freedom to safely share all of this with colleagues and collaborators.

The Ovation Python API wraps the Ovation Java API for use by CPython. Through this Python API, CPython users can access the full functionality of the Ovation ecosystem from within Python. 

Jython users can access the Ovation Java API directly and should *not* use this Python API.


## Requirements

* Java 1.6+
* CPython 2.7+ or 3.3+
* NumPy 1.7+
* Quantities 0.10+

## Technical details

We use the amazing PyLucene JCC library to generate the native wrapper. The wrapper translates between CPython objects and an embedded Java VM via a native Python extension and JNI, the Java Native Interface.

JCC wraps each Java class in the Ovation Java API under the `ovation` python package.

## Building

To build the python wrapper at the command line:

	mvn compile

Build requires:

* Java 1.6 or later
* Maven 3 or later
* CPython 2.7 or later

## Installation

## Usage

This is a code block:

### Connecting to the Ovation database

	>> from ovation import *
	>> from ovation.connection import connect
	>> dsc = connect(<ovation.io user email>)
	Ovation password: <ovation.io password>
	>> context = dsc.getContext()



