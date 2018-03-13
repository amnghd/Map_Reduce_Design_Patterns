#!/usr/bin/python

import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
        if len(line) == 19:
            id = line[3]
            date = line [8]
            hour = date[11:13]
            out_line =[id, hour]
        writer.writerow(out_line)
        

mapper()