#!/usr/bin/env python
"""mapper.py"""
import csv
import sys

# input comes from STDIN (standard input)
csv_data = csv.reader('temp.csv')

print csv_data
