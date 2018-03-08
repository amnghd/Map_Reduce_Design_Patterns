#!/usr/bin/python

import sys

salesTotal = 0
mu = 0
n =0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue
		

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", salesTotal/n
        oldKey = thisKey
        salesTotal = 0
        n = 0

    oldKey = thisKey
    salesTotal += float(thisSale)
    n += 1.0
if oldKey != None:
    print oldKey,"\t",salesTotal/n