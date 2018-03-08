# Combiners:

Combiners are simple reducer performing tasks inside the mapper. Therefore, the mapper basically send out one set of key value pairs instead of pipelining many of them.
This largely reducers the reductions.

```shell
run_mapreduce_with_combiner() {
	hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.1.1.jar -mapper $1 -reducer $2 -combiner $2 -file $1 -file $2 -input $3 -output $4

}

alias hsc=run_mapreduce_with_combiner

```

Afterwards, we run the following inside the shell:

```shell
hsc mapper.py reducer.py  myinput combiner
```


The only thing we need to change is to update the bashrc with a new function and a new alias. Then we need to source the bashrc.

After using combiners, the number of reducer input recors changed to only 28 inputs (7 week days, 4 mappers). Before using combiners, it was ``4,138,476``, which is quite large for only one machine.