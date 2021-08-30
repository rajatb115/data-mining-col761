#!/bin/bash

g++ -o part2a/apriori part2a/apriori.cpp
g++ -o part3/prefixSpan part3/prefixSpan.cpp

module load compiler/gcc/7.1.0/compilervars

cd part2b/fpgrowth/fpgrowth/src/
make all
cd ../../../../


