#!/usr/bin/python
import sys

# used technique in https://github.com/CodeMangler/udacity-hadoop-course/blob/master/src/final-project/top-tags/reducer.py


prevTag = None
currentTag = None
question_id = None
tags = {}
tag_counts = {}


for data in sys.stdin:
    line = data.strip().split("\t")
    if(len(line) == 2):
        currentTag, question_id = line
        print(line)
        if(not tags.has_key(currentTag)):
            tags[currentTag] = []
            tag_counts[currentTag] = 0
        tags[currentTag].append(question_id)
        tag_counts[currentTag] = tag_counts[currentTag] + 1
top_ten_tag_counts = sorted(tag_counts.values())[0:10]
top_ten_tags = map(lambda count_tuple: count_tuple[0], sorted(tag_counts.items(), reverse=True, key=lambda count_tuple: count_tuple[1])[:10])

for tag in top_ten_tags:
    print tag,"\t",len(tags[tag])