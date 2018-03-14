#!/usr/bin/python

import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
        if len(line) == 19:
            post_id, title, tagnames, student, body, node_type = line[:6] 
            parent_id, abs_parent_id, added_at, score = line[6:10]  # getting the student number
            #the mapper generates key-value pairs, where the 
            #key is the node number and the value is the student number. These will later
            #be used inside the reducer to develop a list of collaborators.
            # if the node type is question, pring the post_id, if it is not question,
            #print parentid
            if node_type == "question": 
                print "{0}\t{1}".format(post_id, student) # post id denotes this node
            if node_type != "question": 
                print "{0}\t{1}".format(parent_id, student) #parent id denotes the question node this answer is for

mapper()