#!/bin/bash

VERSION=$1

# On python 3
# if hash pyvenv 2>/dev/null; then
# 	pyenv wrapper.build.env
# else
    /usr/local/bin/virtualenv --distribute wrapper.build.venv
# fi

source wrapper.build.venv/bin/activate

pip install jcc

python "../../src/main/python/build_wrapper.py" "$VERSION" "../../pom.xml"

deactivate

rm -rf wrapper.build.venv