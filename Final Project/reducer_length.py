#!/usr/bin/python
import sys

old_id = None
post_data = None
answers_num = 0
answers_len = 0
answer_flag = 0
question_flag =0

for line in sys.stdin: 
    data_mapped = line.strip().split("\t") 
    post_id, post_type, length = data_mapped 
    length = float(length)
    if post_type == "A":
        answers_num += 1
        answers_len += length
        answer_flag = 1
    
    if post_type == 'Q':
        print post_id,"\t",length,"\t",answers_len/(answers_num+1-answer_flag)
        answer_flag = 0
        answers_num = 0
        answers_len = 0
