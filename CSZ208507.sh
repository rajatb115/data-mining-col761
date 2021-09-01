#!/bin/bash

module load compiler/gcc/7.1.0/compilervars

if [ "$#" -eq 4 ]
then
	if [ "$1" == "-apriori" ]
	then
		cd ./part2a
		./apriori "$2" "$3" "$4.txt"
		mv "$4.txt" ./..
		cd ..
	fi
	
	if [ "$1" == "-prefixspan" ]
	then
		cd ./part3
		./prefixSpan "$2" "$3" "$4.txt"
		mv "$4.txt" ./..
		cd ..
	fi
fi

if [ "$#" -eq 2 ]
then
	if [ "$2" == "-plot" ]
	then
		python3 plot.py "$1"
	fi
fi
