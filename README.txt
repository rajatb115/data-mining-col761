# Data Mining (COL761)

Part A) Apriori implementation: The file apriori.cpp contains an implementation of the apriori algorithm wherein we initially generate a set of frequent items and
then until the candidate set is empty we keep generating frequent itemsets of size 1 greater as we do in apriori and filter to obtain frequent itemsets.


3) Prefix Span Implementation: It is a Depth First technique for sequential pattern mining. The program first extracts all the items present in the input file, containing itemset sequences, and store them lexicographically in a map along with its occurence. At the same time, store the sequence as list of string. 
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


# Contributers
* Rajat Singh
* Chhavi Agarwal
* Shreyans J Nagori
