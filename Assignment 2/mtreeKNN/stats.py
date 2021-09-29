#!/usr/bin/env python
import random
import sys
import time
from mtree import MTree
import functions
import numpy as np
from sklearn.decomposition import PCA
import scipy



REPETITIONS = 3
WORD_LIMIT = None #or 1000
NUM_TEST_WORDS = 3
RATE = 2
TOP_MIN_CAPACITY = 2000
TOP_LIMIT = 500



def rate(start, end, rate_):
	r = start
	while r < end:
		yield r
		r *= rate_



timing = time.time


def create_mtree(words, min_node_capacity):
	print ("Creating M-Tree with min_node_capacity=%r" % min_node_capacity,file=sys.stderr)
	mtree = MTree(min_node_capacity=min_node_capacity, distance_function = functions.euclidean_distance)
	print ("Adding words...",file=sys.stderr)
	b = timing()
	for n, word in enumerate(words, 1):
		mtree.add(tuple(word))
		if n % 100 == 0:
			print ("\r%r words added..." % n,file=sys.stderr)
	e = timing()
	total_time = e - b
	#print >>sys.stderr
	#print "\t".join([
	#		"CREATE-MTREE",
	#		"min_node_capacity=%r" % min_node_capacity,
	#		"total_time=%r" % total_time,
	#		"avg_time=%r" % (total_time / n),
	#])
	
	print ("M-Tree created",file=sys.stderr)
	return mtree



def test(mtree, test_words, min_node_capacity, limit):
	print ("Testing min_node_capacity=%r, limit=%r" % (min_node_capacity, limit),file=sys.stderr)
	for test_word in test_words:
		print ("test_word=%r" % test_word,file=sys.stderr)
		total_time = 0
		for _ in range(REPETITIONS):
			b = timing()
			results = list(mtree.get_nearest(test_word, limit=limit))
			e = timing()
			assert len(results) == limit
			total_time += (e - b)
		
		avg_time = total_time / REPETITIONS
		
		#print "\t".join([
	#			"TEST",
	#			"min_node_capacity=%d" % min_node_capacity,
	#			"test_word=%r" % test_word,
	#			"limit=%d" % limit,
	#			"avg_time=%r" % avg_time
	#	])



def main():
	print ('Loading words...',file=sys.stderr)
	#with open(word_distance.DICT_FILE) as f:
	#	words = list(
	#			itertools.islice(
	#					(line.strip() for line in f.readlines() if line[0] != '%'),
	#					WORD_LIMIT
	#			)
	#	)
	data = np.loadtxt("image_data.dat")
	print(data.shape)
	pca_2 = PCA(n_components=2)
	data_2 = pca_2.fit_transform(data)
	words = data_2
	print(data_2.shape)
	print ('%d words loaded' % len(words),file=sys.stderr)
	
	#test_words = random.sample(words, NUM_TEST_WORDS)
	random_query_2 = np.random.randint(low=1, high=100, size=(100,2), dtype=int)
	print ('Test words:' %random_query_2,file=sys.stderr)
	min_node_capacity=2
	limit=5
	mtree = create_mtree(data_2, min_node_capacity)
	test(mtree, random_query_2, min_node_capacity, limit)
	
	#for min_node_capacity in (int(r) for r in rate(2, TOP_MIN_CAPACITY, RATE)):
	#	mtree = create_mtree(data_2, min_node_capacity)
		
	#	for limit in (int(r) for r in rate(1, TOP_LIMIT, RATE)):
	#		test(mtree, random_query_2, min_node_capacity, limit)



if __name__ == "__main__":
	main()
