# Data Mining (COL761) - Homework 2

# Contributers

Rajat Singh - 2020CSZ8507
Chhavi Agarwal - 2020CSY7654
Shreyans J Nagori - 2018CS10390


# Implementation :

To run Q1.sh and Q2.sh in hpc we need to load some modules. We tried loading various combination of the the modules but this is the final module list that is required to be loaded before execution of these files.

module load compiler/gcc/7.1.0/compilervars
module load pythonpackages/3.6.0/matplotlib/3.0.2/gnu
module load pythonpackages/3.6.0/scipy/1.1.0/gnu
module load compiler/intel/2019u5/intelpython3
module load pythonpackages/3.6.0/numpy/1.16.1/gnu

Note - We tried to run the code after loading these modules in different order but the code didn't worked and raised various exceptions. It is recommended to load these modules in the same order as given.

Q1 - To run Q1.sh script use the command given below. It will generate the running time vs support threshod plot for FSG , gSpan and Gaston.
      sh Q1.sh <data> <plot_name>

Q2  - To run Q2.sh script use the command given below. It will generate the running time vs dimentions plot for k-NN query on KD-Tree, M-Tree and Bruteforce.
      sh Q2.sh <data> <plot_name>
      
# Note
1. Our code will take the raw (unprocessed) data as given in the assignment and generate the plot.
2. HPC was behaving very weirdly while running these algorithms. We were getting variation in running time of the algorithms every time, this is due to the loding time of some pre-requsite modules used by these algorithms, some time they get loaded very fast and othertimes slow.
