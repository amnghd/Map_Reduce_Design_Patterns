# Testing Instruction:

"

## Final Project: Local Testing Instructions

We have created a smaller dataset that you can use to easily test your code for the Final Project for Intro to Hadoop and MapReduce. To do so, please follow these steps:

1. Make sure that all of your code for the Final Project is saved in the same folder on your machine.

2. Download the test data here. 

3. Save the test data file you just downloaded (it's called student_test_posts.csv) in the same folder as your code for the Final Project. 

4. For each exercise in the Final Project, repeat steps 5 through 7 with the proper file names. The example used here is the Student Times exercise. 

5. Open up a terminal or command line window on your computer, and navigate to the folder where your Final Project code and student_test_posts.csv are.

6. Run the following command to display your code’s output: $ cat student_test_posts.csv | python student_times_mapper.py | sort | python student_times_reducer.py

7. Compare your results to the corresponding expected output: 

- Student Times expected output

- Post and Answer Length expected output

- Top Tags expected output

- Study Groups expected output

"



Project #1: {mapper,reducer}_length.py

**Students and Posting Time on Forums**

We have a lot of passionate students that bring a lot of value to forums. Forums also sometimes need a watchful eye on them, to make sure that posts are tagged in a way that helps to find them, that the tone on forums stays positive, and in general - they need people who can perform some management tasks - forum moderators. These are usually chosen from students who already have shown that they are active and helpful forum participants.
Our students come from all around the world, so we need to know both at what times of day the activity is the highest, and to know which of the students are active at that time.
In this exercise your task is to find for each student what is the hour during which the student has posted the most posts. Output from reducers should be:
author_id    hour
For example:
13431511\t13
54525254141\t21
If there is a tie: there are multiple hours during which a student has posted a maximum number of posts, please print the student-hour pairs on separate lines. The order in which these lines appear in your output does not matter.
You can ignore the time-zone offset for all times - for example in the following line: "2012-02-25 08:11:01.623548+00" - you can ignore the +00 offset. 
In order to find the hour posted, please use the date_added field and NOT the last_activity_at field.
To make sure your code is running properly, we have put together a smaller data set and set of expected outputs for you to use to check your work. Please click here to access the instructions to use it.





Project #2 : {mapper,reducer}_student_time.py

We are interested to see if there is a correlation between the length of a post and the length of answers. 
Write a mapreduce program that would process the forum_node data and output the length of the post and the average answer (just answer, not comment) length for each post. You will have to decide how to write both the mapper and the reducer to get the required result.


Project #3: {mapper,reducer}_top10.py

We are interested seeing what are the top tags used in posts.
Write a mapreduce program that would output Top 10 tags, ordered by the number of questions they appear in.
For an extra challenge you can think about how to get a top 10 list of tags, where they are ordered by some weighted score of your choice. If you decide to do this, then please submit your solution to the regular problem and then also submit this extra challenge problem in separate files as described on the instruction page.
To make sure your code is running properly, we have put together a smaller data set and set of expected outputs for you to use to check your work. Please click here to access the instructions to use it.
Please note that you should only look at tags appearing in questions themselves (i.e. nodes with node_type "question"), not on answers or comments.
Hints for writing reducer code
Code should not use a data structure (e.g. a dictionary) in the reducer that stores a large number of keys. Remember that Hadoop already sorts the mapper output based on key, such that key-value pairs with the same key will appear consecutively as input to the reducer. Make sure you take advantage of this ordering when you write your reducer code.
Please feel free to use dictionaries to process data for the current key, but you shouldn't keep old data around from previous keys (eg. in a dictionary) if you don't need to. 
This is part of a more general principle connected with the Volume characteristic of Big Data. Mappers and reducers read through very large amounts of data and we should be mindful, as we write mapper and reducer code, of how much data we store in main memory.



Project # 4: {mapper,reducer}_studgroup.py

We might want to help students form study groups. But first we want to see if there are already students on forums that communicate a lot between themselves.
As the first step for this analysis we have been tasked with writing a mapreduce program that for each forum thread (that is a question node with all it's answers and comments) would give us a list of students that have posted there - either asked the question, answered a question or added a comment. If a student posted to that thread several times, they should be added to that list several times as well, to indicate intensity of communication.
To make sure your code is running properly, we have put together a smaller data set and set of expected outputs for you to use to check your work. Please click here to access the instructions to use it.
Hints for writing reducer code
Code should not use a data structure (e.g. a dictionary) in the reducer that stores a large number of keys. Remember that Hadoop already sorts the mapper output based on key, such that key-value pairs with the same key will appear consecutively as input to the reducer. Make sure you take advantage of this ordering when you write your reducer code.
This is part of a more general principle connected with the Volume characteristic of Big Data. Mappers and reducers read through very large amounts of data and we should be mindful, as we write mapper and reducer code, of how much data we store in main memory.

results:
```
111 	['100000066']
15084 	['100004819']
2 	['100000005']
262 	['100004819']
26454 	['100003192']
3778 	['100000066', '100008254']
6011204 	['100010128', '100020526', '100071170']
6011936 	['100004819', '100019875', '100071170']
6012754 	['100004819', '100012200']
6015491 	['100004467', '100005156', '100071170']
66193 	['100002460', '100004467', '100007808', '100071170']
7185 	['100003268']
parent_id 	['author_id']

```