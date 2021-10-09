#!/bin/bash

# clone the repository from github
repo="https://github.com/rajatb115/data-mining-col761.git"
git clone "$repo"

folder="data-mining-col761"
cd "$folder"

# file="CSZ208507-Assgn1.zip"
# unzip "$file"

# loading relevent version of compilers
# module load compiler/gcc/7.1.0/compilervars
# module load compiler/python/3.6.0/ucs4/gnu/447
# module load compiler/intel/2019u5/intelpython3

# loading relevent libraries
# module load pythonpackages/3.6.0/matplotlib/3.0.2/gnu
# module load pythonpackages/3.6.0/scipy/1.1.0/gnu
# module load pythonpackages/3.6.0/numpy/1.16.1/gnu

module load compiler/gcc/7.1.0/compilervars
# module load compiler/intel/2019u5/intelpython3
module load pythonpackages/3.6.0/matplotlib/3.0.2/gnu
module load pythonpackages/3.6.0/scipy/1.1.0/gnu
module load compiler/intel/2019u5/intelpython3
module load pythonpackages/3.6.0/numpy/1.16.1/gnu
