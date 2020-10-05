#!/bin/bash

if [ ! -d .pyenv ]; then
    git clone https://github.com/pyenv/pyenv .pyenv
fi

if [ ! -d .pyenv/plugins/pyenv-virtualenv ]; then
    git clone https://github.com/pyenv/pyenv-virtualenv.git .pyenv/plugins/pyenv-virtualenv
fi

. ./init.sh

pyenv install -s 3.6.9
pyenv virtualenv -f 3.6.9 cording_api
