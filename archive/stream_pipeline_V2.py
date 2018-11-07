# python 3 
# ref 
# https://medium.com/data-science-school/practical-apache-spark-in-10-minutes-part-5-streaming-b3b42dbeae63


from pyspark import SparkContext
from pyspark.streaming import StreamingContext


if __name__ == '__main__':
	sc = SparkContext("local[2]",appName="PythonStreamingCountByValue")
	ssc = StreamingContext(sc, 30)
	ds = ssc.socketTextStream("localhost", 9999)
	data = ds.flatMap(lambda line: int(line.split(" ")[0]))
	data_count = data.countByValue()
	data_count.pprint()
	print (data_count)
	ssc.start()
	ssc.awaitTermination()