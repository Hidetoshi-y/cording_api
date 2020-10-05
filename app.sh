#!/bin/bash

DIR=$(dirname $0|sed -e "s|^\.$|$PWD|")
#echo $DIR

. $DIR/init.sh
pyenv local $REPO

######################################################################
    
exec python3 $DIR/app.py
