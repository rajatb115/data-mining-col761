#!/bin/bash

tmp=$1

if [ $tmp -eq 0 ]
then
    python3 Q2/fin_code_2.py
else 
    python3 Q2/fin_code_2_model.py
fi
