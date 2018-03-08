#!/usr/bin/python


import sys
from datetime import datetime
week_map = {0:'M', 1:'Tu',2:'We', 3:'Th', 4:'F',5:'Sa', 6:'Su'}
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        week_num = datetime.strptime(date, "%Y-%m-%d").weekday()
        weekday = week_map[int(week_num)]
        print "{0}\t{1}".format(weekday, cost)