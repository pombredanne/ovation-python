#!/bin/bash

VERSION=$1

# On python 3
# pyenv wrapper.build.env
/usr/local/bin/virtualenv --distribute wrapper.build.venv

source wrapper.build.venv/bin/activate

pip install jcc

python "../../src/main/python/build_wrapper.py" "$VERSION" "../../pom.xml"

deactivate

rm -rf wrapper.build.venv