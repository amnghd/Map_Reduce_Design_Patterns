# Structural [Hierarchical] Patterns:

These are very pragmatic patterns becuase they allow us to move from Relationaml Database Management Systems to Hadoop.

You can use this to join tables.

The conditions for this migration is:

1- Data must be linked using foreign keys

2- Data must be structured and row based

Basically, having a similar key is how we combine the two datasets.


"""
Your goal for this task is to write mapper and reducer code 
that will combine some of the forum and user data. 
In relational algebra, this is known as a join operation. 
At the moment, this is not an auto-gradable exercise, but instructions below are given on how to test your code on your machine. 

The goal is to have the output from the reducer with the following fields for each forum post: 
"id" 0 "title"1  "tagnames"2  "author_id"3  "node_type"4  "parent_id"5  "abs_parent_id"6  "added_at"7 
"score"8  "reputation"9  "gold"10  "silver"11  "bronze"12
 
Note that for each post we have taken some of the information describing the post, 
and joined it with user information. The body of the post is not included in the final output. 
The reason is that it is difficult to handle a multiline body, as it might be split on separate 
lines during the intermediate steps Hadoop performs - shuffle and sort.   

Your mapper code should take in records from both forum_node and forum_users. 
It needs to keep, for each record, those fields that are needed for the final output given above. 
In addition, mapper needs to add some text (e.g. "A" and "B") to mark where each output comes from 
(user information vs forum post information). Example output from mapper is:

"12345"  "A"  "11"  "3"  "4"  "1"
"12345"  "B"   "6336" "Unit 1: Same Value Q"  "cs101 value same"  "question"  "\N"  "\N"  "2012-02-25 08:09:06.787181+00"  "1" 
  
The first line originally comes from the forum_users input. It is from a student with user id: 12345 - the mapper key. 
The next field is the marker A specifying that the record comes from forum_users. 
What follows is the remaining information user information. 

The second line originally comes from the forum_node input. 
It also starts with the student id (mapper key) followed by a marker B and the information about the forum post.  
   
The mapper key for both types of records is the student ID: 
"user_ptr_id" from "forum_users" or  "author_id" from "forum_nodes" file. 
Remember that during the sort and shuffle phases records will be grouped based on the student ID (12345 in our example). 
You can use that to process and join the records appropriately in the reduce phase. 
"""


# Procedure:

First we put both forum data inside a hadoop folder to provide it later for the job.

forum user header:

"user_ptr_id" [0]	"reputation" [1]	"gold" [2]	"silver" [3]	"bronze" [4] all of these are needed


forum_node header:

"id"3	** "title"1	"tagnames"2	"author_id"**0	"body"4	**"node_type"5	"parent_id"6	"abs_parent_id"7	"added_at"8	"score"**9	"state_string"10	"last_edited_id"11	"last_activity_by_id"12	"last_activity_at"13	"active_revision_id"14"extra"15	"extra_ref_id"16	"extra_count"17	"marked"18


# Results:

Take a look at mapper.py and reducer.py. After running this code, the tables, though in HDFS format will join as if they are in relational database management system.

The results are also uploaded in a text file. Here is a snapshot of it.

```
"100000002"	""	"cs101 "	"10273"	"answer"	"1335"	"1335"	"2012-02-29 09:30:12.560234+00"		"6"	"0"	"0"	"2"
"100000003"	""	"cs373 "	"1000081"	"comment"	"1000074"	"1000021"	"2012-02-21 05:23:27.537634+00"					
"100000005"	"Russian Group"	"cs373 russian study groups"	"1000021"	"question"	"\N"	"\N"	"2012-02-21 04:01:59.622992+00"		"583"	"2"	"3"	"11"
"100000007"	""	"cs101 "	"14"	"answer"	"2"	"2"	"2012-02-21 03:48:37.977542+00"					
"100000008"									"735"	"0"	"1"	"9"
"100000009"	""	"technical-support "	"4000172"	"answer"	"4000053"	"4000053"	"2012-04-23 16:51:33.208017+00"		"5"	"0"	"0"	"0"
"100000011"	""	"cs373 "	"1016929"	"answer"	"1001614"	"1001614"	"2012-03-10 06:39:43.076821+00"					
"100000014"	""	"cs101 "	"30"	"answer"	"15"	"15"	"2012-02-21 03:55:43.509325+00"		"91"	"0"	"2"	"6"
```
