#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    columns = line.split(',') # split line into parts
    # the data is messy, only read those having correct column count
    if len(columns) == 14:
        try:
            countUpVotes = int(columns[7])
            print "%s\t%s" % (columns[8],countUpVotes)
        except ValueError:
            pass