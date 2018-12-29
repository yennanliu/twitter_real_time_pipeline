# python 3 


# May cause deprecation warnings, safe to ignore, they aren't errors
# spark 
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import SQLContext
from pyspark.sql.functions import desc
from collections import namedtuple
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext, Row
# op 
import time 


#--------------------------------------------------
# help func 
# Lazily instantiated global instance of SQLContext
def getSqlContextInstance(sparkContext):
    if ('sqlContextSingletonInstance' not in globals()):
        globals()['sqlContextSingletonInstance'] = SQLContext(sparkContext)
    return globals()['sqlContextSingletonInstance']



def process(time, rdd):
    print("========= %s =========" % str(time))
    try:
        # Get the singleton instance of SQLContext
        sqlContext = getSqlContextInstance(rdd.context)

        # Convert RDD[String] to RDD[Row] to DataFrame
        rowRdd = rdd.map(lambda w: Row(word=w))
        wordsDataFrame = sqlContext.createDataFrame(rowRdd)

        # Register as table
        wordsDataFrame.registerTempTable("words")

        # Do word count on table using SQL and print it
        wordCountsDataFrame = sqlContext.sql("select word, count(*) as total from words group by word")
        wordCountsDataFrame.show()
    except:
        pass

#--------------------------------------------------




if __name__ == '__main__':
	# PART 1) : BASIC STREAMING 
	# CONFIG
	# create a SparkContext object with 2 local threads
	# name it as "NetworkWordCount"
	sc = SparkContext('local[2]', 'NetworkWordCount')
	
	fields = ("tag", "count" )
	Tweet = namedtuple( 'Tweet', fields )

	print (sc)
	# pass a SparkContect to a StreamingContext object 
	# with batch duration = e.g. 10s
	ssc = StreamingContext(sc, 10)
	socket_stream = ssc.socketTextStream("127.0.0.1", 9999)
	# set where the data streaming will come from e.g. localhost:9999
	lines = socket_stream.window( 20 )
	# split the 'lines' with a whitespace into a list of words
	words = lines.flatMap( lambda text: text.split( " " ))
	# create a tuple of each word and 1 using 'map'
	# e.g. word_0 --> (word_0, 1)
	pairs = words.map(lambda word: (word, 1))
	# count the words using reduceByKey e.g. by 'word_0', 'word_1'
	word_counts = pairs.reduceByKey(lambda num1, num2: num1 + num2)
	# print elements of the RDD
	word_counts.pprint()
	print (word_counts)
	# in case just run on PART 1) 
	#ssc.start()
	#ssc.awaitTermination()  # Wait for the computation to terminate


	# PART 2) SPARK SQL IN STREAMING WINDOW 
	words.foreachRDD(process)

	ssc.start()
	ssc.awaitTermination()  # Wait for the computation to terminate









