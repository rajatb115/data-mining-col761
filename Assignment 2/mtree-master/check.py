#!/usr/bin/env python
import random
import sys
import time
import mtree
import numpy as np
from sklearn.decomposition import PCA
import scipy
import math




def d_int(x, y):     
    return abs(x - y)

def euclidean_distance(data1, data2):
	distance = 0
	for v1, v2 in zip(data1, data2):
		diff = v1 - v2
		distance += diff * diff
	distance = math.sqrt(distance)
	return distance

def main():
	print ('Loading words...',file=sys.stderr)
	data = np.loadtxt("image_data.dat")
	print(data.shape)
	pca_2 = PCA(n_components=2)
	data_2 = pca_2.fit_transform(data)
	print(data_2.shape)
	print ('%d words loaded' % len(data_2),file=sys.stderr)
	
	random_query_2 = np.random.randint(low=1, high=100, size=(100,2), dtype=int)
	print ('Test words:' %random_query_2,file=sys.stderr)

	tree = mtree.MTree(euclidean_distance, max_node_size=4)
	for n, word in enumerate(data_2, 1):
		tree.add(tuple(word))
		if n % 1000 == 0:
			print ("\r%r words added..." % n,file=sys.stderr)

	for test_word in random_query_2:
		tw = tuple(test_word)
		print ("test_word=%r",tw,file=sys.stderr)
		results = list(tree.search(tw, 5))
		print(results)
		assert len(results) == 5

if __name__ == "__main__":
	main()
