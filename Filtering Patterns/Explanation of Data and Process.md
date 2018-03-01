## Filters:

Filters are the first of map reduce patterns. They don't modify the main data set and mainly provide a subset of it.

These are exaples of filters:

1. Simple filters

2. Bloom filter (probablistic)

3. Sampling

4. Random sampling

5. Top - N


## Data Importin
"The data in at least one of the fields (the body field) can include newline characters, and all the fields are enclosed in double quotes.
Therefore, we will need to process the data file in a way other than using split(",").
To do this, we have provided sample code for using the csv module of Python.
Each 'line'will be a list that contains each field in sequential order.

In this exercise, we are interested in the field 'body' (which is the 5th field, line[4]).
The objective is to count the number of forum nodes where 'body' either contains none of the three punctuation marks:
period ('.'), exclamation point ('!'), question mark ('?'), or else 'body' contains exactly one such punctuation mark as thelast character.
There is no need to parse the HTML inside 'body'. Also, do not pay special attention to newline characters."