#!/bin/bash

tmp=$1

if [tmp == 0]
then
    python3 Q2/fin_code2.py
else 
    python3 Q2/fin_code2_model.py
fi
