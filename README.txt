# Data Mining (COL761) - Homework 1

# Contributers

Rajat Singh - 2020CSZ8507
Chhavi Agarwal - 2020CSY7654
Shreyans J Nagori - 2018CS10390


Implementation :

install.sh - This scrip file is used to clone the current repository and load the correct version of dependencies in HPC. After running this script it will clone the repository in the current working directory.

compile.sh - This script is used to generate the executable (binary) files to their respective locations, that will be used by CSZ208507.sh scrip.

CSZ208507.sh - This scrip is used to run various implemented algorithms ( Apriori, Fp-tree and PrefixSpan ) and generate their output.
	
To run Apriori Algorithm and generate frequent itemsets we will use the following command where X is the minimum support threshold, input_dataset is a dataset on which we are running the algorithm and <filename> is the name of the output file. It will create "filename.txt" as output file and save the frequent itemsets in it.
		
		./CSZ208507.sh -apriori <input_dataset> X <filename>

To compare performance between Apriori and FP-tree implementation and plot graph for the comparison we will use the following command where input_dataset is the dataset on which we are running the algorithm. This script will run the Apriori and FP-tree algorithms on various minimum support threshold on the given dataset and create "plot.png" as output file and save it inside "output" folder.
		
		./CSZ208507.sh <input_dataset> -plot

To run PrefixSpan Algorithm and generate frequent itemsets we will use the following command where X is the minimum support threshold, input_dataset is a dataset on which we are running the algorithm and <filename> is the name of the output file.It will create "filename.txt" as output file and save the frequent itemsets in it.

		./CSZ208507.sh -prefixspan <input_dataset> X <filename>


Question 2:
 
Part A) Apriori implementation: 

The file apriori.cpp contains an implementation of the apriori algorithm wherein we initially generate a set of frequent items and
then until the candidate set is empty we keep generating frequent itemsets of size 1 greater as we do in apriori and filter to obtain frequent itemsets. 


Part B) Performance comparison between Apriori and FP-tree implementation:

In this part we are comparing the running time of Apriori algorithm with running time of FP-tree algorithm. We have used plot.py script to run Apriori and FP-tree algorithm on various minimum support threshold and plot a graph showing the running time of both the algorithms on those thresholds. The plot of the graph will be saved in "output" folder with the name of "plot.png". After running the script we can conclude that with the decrease in the minimum threshold support the time taken by Apriori algorithm is increasing exponentially. Even for 5% and 10% threshold it is taking more than 8 hrs to generate the result for the given test dataset(webdocs.dat). On the other hand FP-tree algorithm takes far less time as compared to Apriori algorithm, thus we are able to run FP-tree algorithm even for 5% and 10% threshold for the given dataset under 5 mins.

The reason for getting this trend as shown in the graph is as follows:
- Apriori algorithm is an array based algorithm and it use Join and Prune technique to generate the candidates but FP-growth is a tree based algorithm which constructs conditional frequent pattern tree and conditional pattern base from database which satisfy minimum support.
- Since there are large amount of candidate generation occurred in Apriori algorithm thus it take huge amount of space on the other hand FP-tree require less amount of space due to compact structure and there is no candidate generation in case of FP-growth.
- While generating candidate set Apriori algorithm have to scan the dataset(database) a lot of times but FP-growth scans the dataset(database) only twice which increase the speed of FP-growth.
- In Apriori algorithm at each step we are generating candidates that will increase exponentially at each step thus make it very slow.


Question 3:

Prefix Span Implementation: 

File: prefixSpan.cpp

It is a Depth First technique for sequential pattern mining. The program first extracts all the items present in the input file, containing itemset sequences, and store them lexicographically in a map along with its occurence. At the same time, store the sequence as list of string. 
The second step is pruning. Prune all the items which have occurence less than the minimum support required. For all the frequent items, we will create projected database and find the frequent subsequqnce of size i+1, using Depth First approach via recursion. 

void frequent_sequence(vector<list<string>> database, map<string,int> link, string key, int sup, string seq, int iter); implements recursion.

database: projected database for current iteration.
link: pruned list of items
key: item to test, if its subsequence is frequent or not
sup: support value required
seq: the current frequent subsequence


First create new projected database from the current projected database for the item "key". Then count the support for all items in pruned map "link" and make new map, storing the results. Again prune the map removing the items whose occurence is less than the support.
Print the frequent subsequence in the output file.
Append the pruned items in the frequent subsequence and call the recursive function for all items appended.

The output file does not contain an extra empty line after printing the last sequence.

File: path.txt

It contains the raw data taken from the site

File: paths_finished.dat

It contains the pre-preocessed data where items are seperated by ';'

File: UpdatedFile.cpp

Pre-process the file path.txt and store the data in file paths_finished.dat
It reads path.txt line by line, process the line by spliting on ";". If it encounters anything except "<", it pushes it into the stack, else it pops the top entry on stack and replaces the current "<" by the current top element in the stack and continue similarly with the rest of the items in that sequence.

File: frequent_path.txt

It stores the output of prefixSpan applied on sequences in paths_finished.dat with support of 1%.

