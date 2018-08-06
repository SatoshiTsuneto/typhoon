#!/bin/bash

# output text write to text file
python getText.py >> typhoon.txt

# get typhoon coordinate
python getCoordinate.py

# del text file
rm typhoon.txt
