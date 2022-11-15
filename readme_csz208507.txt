# Data Mining (COL761) - Homework 3

# Contributers

Rajat Singh - 2020CSZ8507
Chhavi Agarwal - 2020CSY7654
Shreyans J Nagori - 2018CS10390

# Part 1

To run the code for Q1:
./Q1.sh

To run the code for Q2 : 
./Q2.sh 0 (for training from scratch)
./Q2.sh 1 (for using the already trained model)


# Installation of modules:
All the modules were already installed in our HPC account so our code was running without any error in hpc.
In case if requirement is not satisfied, then you can install these libraries before running the code in the same order.

pip3 install torch-scatter -f https://pytorch-geometric.com/whl/torch-${TORCH}+${CUDA}.html --user
pip3 install torch-sparse -f https://pytorch-geometric.com/whl/torch-${TORCH}+${CUDA}.html --user
pip3 install torch-cluster -f https://pytorch-geometric.com/whl/torch-${TORCH}+${CUDA}.html --user
pip3 install torch-spline-conv -f https://pytorch-geometric.com/whl/torch-${TORCH}+${CUDA}.html --user
pip3 install torch-geometric -f https://pytorch-geometric.com/whl/torch-${TORCH}+${CUDA}.html --user

we are using the Python 3.6.10 and GCC 7.3.0 for running the code.
