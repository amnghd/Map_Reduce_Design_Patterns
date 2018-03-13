#!/usr/bin/python
import sys

start = 1
oldKey = None
hour_dict = {}
hour_set = set()
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue
    thisKey, hour = data_mapped
    thisHour = hour[1:-1]

    if oldKey and oldKey != thisKey:
        max_value = max(hour_dict.values())
        max_keys = [k for k, v in hour_dict.items() if v == max_value]
        for i in range(len(max_keys)):
            print oldKey,"\t",max_keys[i]
        oldKey = thisKey;
        hour_set = set()
        hour_dict = {}
        start = 1
    if (oldKey == thisKey) or (start ==1):
        start = 0        
        if thisHour in hour_set:
            hour_dict[thisHour] += 1
        if thisHour not in hour_set:
            hour_set.update([thisHour])
            hour_dict[thisHour] = 1
    oldKey = thisKey

if oldKey != None:
    print oldKey,"\t",max_keys