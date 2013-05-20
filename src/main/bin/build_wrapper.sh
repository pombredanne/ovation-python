#!/bin/bash

VERSION=$1

if [[ -z $NO_VENV ]] ; then
	# On python 3
	path_to_pyenv=$(which pyenv)
	 if [ -x "$path_to_executable" ] ; then
	    path_to_pyenv wrapper.build.env
	else
	    /usr/local/bin/virtualenv --distribute wrapper.build.venv
	fi

	source wrapper.build.venv/bin/activate

	pip install jcc
fi

python "../../src/main/bin/build_wrapper.py" "$VERSION" ../../pom.xml "-Pjenkins"


if [[ -z $NO_VENV ]] ; then
	deactivate

	rm -rf wrapper.build.venv
fi