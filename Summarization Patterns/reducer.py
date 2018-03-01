#!/usr/bin/python
import sys

fantastic_number = 0
fantastically_list = list()

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue
    word, node = data
    word = word.strip()
    node = node.strip()
    if word == 'fantastic':
        fantastic_number += 1
    if word == 'fantastically':
        fantastically_list.append(node)

print "fantstic word occured {0} times".format(fantastic_number)

print "fantastically occured in {0}".format(fantastically_list)
