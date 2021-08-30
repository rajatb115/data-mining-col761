#!/bin/bash

# clone the repository from github
repo="https://github.com/rajatb115/data-mining-col761.git"
git clone "$repo"

folder="data-miningcol761"
cd "$folder"

file="CSZ208507-Assgn1.zip"
unzip "$file"

# load relevent version of compilers
module load compiler/gcc/7.1.0/compilervars
