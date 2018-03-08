This section is dedicated to performing statistical summarization on data.
This means that we want to calculate summary statistics for different parameters.


For such purpose, the mapper generates a key value pair, where key is the day of the week and value is the purchase. The mapper pipes this data to the reducer.
Then the reducer performs the mean calculation from the mapped data.

Sample results will be similar to this:

```

F 	250.223089314
M 	250.009331149
Sa 	250.084703253
Su 	249.946443251
Th 	249.872024327
Tu 	249.738227929
We 	249.851167194

```