#!/bin/bash

VERSION=$1

# On python 3
path_to_pyenv=$(which pyenv)
 if [ -x "$path_to_executable" ] ; then
    path_to_pyenv wrapper.build.env
else
    /usr/local/bin/virtualenv --distribute wrapper.build.venv
fi

source wrapper.build.venv/bin/activate

pip install jcc

python "../../src/main/python/build_wrapper.py" "$VERSION" "../../pom.xml" "-Pjenkins"

deactivate

rm -rf wrapper.build.venv