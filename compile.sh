#!/bin/bash

module load compiler/gcc/7.1.0/compilervars

g++ -o part2a/apriori part2a/apriori.cpp
g++ -o part3/prefixSpan part3/prefixSpan.cpp

cd part2b/fpgrowth/fpgrowth/src/
make all
cd ../../../../

chmod 777 compile.sh
chmod 777 install.sh
chmod 777 CSZ208507.sh
chmod 777 part2a/apriori
chmod 777 part3/prefixSpan
chmod 777 part2b/fpgrowth/fpgrowth/src/fpgrowth
