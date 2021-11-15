#!/bin/bash

# clone the repository from github
repo="https://github.com/rajatb115/data-mining-col761.git"
git clone "$repo"

folder="data-mining-col761"
cd "$folder"

file="HW3_csz208507.zip"
unzip "$file"

cd "HW3_csz208507"

chmod 777 "Q2.sh"
chmod 777 "Q1.sh"

module load compiler/gcc/7.1.0/compilervars
module load compiler/intel/2019u5/intelpython3
