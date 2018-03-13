#!/usr/bin/python

import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
        if len(line) == 19:
            post_id, title, tagnames, user_id, body, node_type = line[:6] 
            parent_id, abs_parent_id, added_at, score = line[6:10] 

            if post_id == 'id': 
                continue 
            if node_type == "question": 
                print "{0}\t{1}\t{2}".format(post_id, "Q", len(body)) 
            if node_type == "answer": 
                print "{0}\t{1}\t{2}".format(parent_id, "A", len(body))
        

mapper()
