#!/bin/bash

chmod 777 compile.sh
./compile.sh

python3 Q2/part2.py "$1" "$2.png"
