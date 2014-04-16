#!/bin/bash
# - Aim to build up pinet development evironmnet.
# - Author: tim.tang

if [ ! -e venv ]; then
    virtualenv --no-site-packages venv
fi

source venv/bin/activate
export STATIC_DEPS=true
pip install -r devel-req.txt
