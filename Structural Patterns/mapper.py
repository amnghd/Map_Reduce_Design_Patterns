#!/usr/bin/python


import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
        if len(line) == 5:
            id, rep, gold, silv, bron = line
            out_line = [id, "U", rep, gold, silv, bron]
        if len(line) == 19:
            out_line = [line[3], "N", line[1], line[2], line[0], line[5], line[6], line[7], line[8], line[9] ]
        writer.writerow(out_line)
        

mapper()