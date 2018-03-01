#!/usr/bin/python

import sys
import re
import csv


reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)



for line in reader:
    data = line
    if len(data) == 19:
        node, title ,tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, scors, state_string, last_edited_id, last_activity_by_id, last_activity_at, active_revision_id,extra, extra_ref_id, extra_count, marked = data
        body_list = re.split(r"[\s\.,!\?:;\"\(\)\<\>#$\=\-\/]+", body)
        for item in body_list:
            print item.lower(),"\t",node

