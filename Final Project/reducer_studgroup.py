#!/usr/bin/python
import sys

old_key = None
collaborators = [] #this list will be used form the list of collaborators
for line in sys.stdin: 
    line_list = line.strip().split("\t")
    if len(line_list) != 2:
        continue
    node, student = line.strip().split("\t")
    this_key = node

    if old_key and old_key != this_key:
        print old_key,"\t",collaborators
        collaborators = []

    collaborators.append(student)
    
    old_key = this_key

if old_key:
    print old_key,"\t",collaborators