#!/bin/bash

VERSION=$1

/usr/local/bin/virtualenv --distribute wrapper.build.venv
# On python 3
# pyenv wrapper.build.env
source wrapper.build.venv/bin/activate

pip install jcc

python "../../src/main/python/build_wrapper.py" "$VERSION" "../../pom.xml"

deactivate

rm -rf wrapper.build.venv

# rename org.apache.commons.lang.enums.Enum=CLEnum 