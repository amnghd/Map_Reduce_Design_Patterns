#!/usr/bin/python

import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
        if len(line) == 19:
            tagnames = line[2].strip().split(" ")
            for i in range(len(tagnames)):
                print tagnames[i],"\t",tagnames[i]

mapper()