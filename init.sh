#!/bin/bash

BASE=/data/home/yoshida
REPO=cording_api
PYTHON=3.6.9

DIR=$BASE/$REPO
#echo $DIR

unset PYENV_ROOT
unset VIRTUAL_ENV
unset PYENV_VIRTUAL_ENV

export PYENV_ROOT=$DIR/.pyenv
export PATH="$PYENV_ROOT/bin:$PATH"
if type pyenv >/dev/null 2>&1; then
    eval "$(pyenv init - --no-rehash)"
    eval "$(pyenv virtualenv-init -)"
else
    echo pyenv not found, exit.
    exit 1
fi
