#!/bin/bash

chmod 777 compile.sh
./compile.sh

a=`pwd`
echo $a

python3 plot.py "$1" "$2.png"
