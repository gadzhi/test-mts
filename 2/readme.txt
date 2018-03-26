Файл mapper.py представляет собой реализацию MapReduce на python без использования Hadoop

Файл test_map_reduce.py - реализация на Hadoop  c помощью библиотеки pywebhdfs

Так же задачу можно реализовать помощью Hadoop CLI

Еще одна реализация через Hadoop Streaming выглядит так:

yarn jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar\
 -input csv\
 -output csv_out\
 -file mapper.py\
 -file reducer.py\
 -mapper "python mapper.py"\
 -reducer "python reducer.py"