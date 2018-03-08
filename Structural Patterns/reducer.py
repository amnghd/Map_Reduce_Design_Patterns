#!/usr/bin/python
# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

import sys


def reducer():
    oldKey = None
    total_list = ["" for _ in range(13)]
    for line in sys.stdin:
        data_mapped = line.strip().split("\t")
        thisKey = data_mapped[0]


        if data_mapped[1][1]== "U":
            total_list[0] = data_mapped[0]
            total_list[9] = data_mapped[2]
            total_list[10] = data_mapped[3]
            total_list[11] = data_mapped[4]
            total_list[12] = data_mapped[5]
        
        if data_mapped[1][1] == "N":
            total_list[0] = data_mapped[0]
            total_list[1] = data_mapped[2]
            total_list[2] = data_mapped[3]
            total_list[3] = data_mapped[4]
            total_list[4] = data_mapped[5]
            total_list[5] = data_mapped[6]
            total_list[6] = data_mapped[7]
            total_list[7] = data_mapped[8]

        if oldKey and oldKey != thisKey:
            print "\t".join(total_list)
            oldKey = thisKey;
            total_list = ["" for _ in range(13)]
               
        oldKey = thisKey

    if oldKey != None:
        print "\t".join(total_list)

reducer()