

# May cause deprecation warnings, safe to ignore, they aren't errors
# spark 
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import SQLContext
from pyspark.sql.functions import desc
from collections import namedtuple
# op 
import time 


# Can only run this once. restart your kernel for any errors.
sc = SparkContext()
ssc = StreamingContext(sc, 10 )
sqlContext = SQLContext(sc)
socket_stream = ssc.socketTextStream("127.0.0.1", 9999)
lines = socket_stream.window( 20 )
fields = ("tag", "count" )
Tweet = namedtuple( 'Tweet', fields )

# run 
# Use Parenthesis for multiple lines or use \.
( lines.flatMap( lambda text: text.split( " " ) ) #Splits to a list
  .filter( lambda word: word.lower().startswith("#") ) # Checks for hashtag calls
  .map( lambda word: ( word.lower(), 1 ) ) # Lower cases the word
  .reduceByKey( lambda a, b: a + b ) # Reduces
  .map( lambda rec: Tweet( rec[0], rec[1] ) ) # Stores in a Tweet Object
  .foreachRDD( lambda rdd: rdd.toDF().sort( desc("count") ) # Sorts Them in a DF
  .limit(10).registerTempTable("tweets") ) ) # Registers to a table.

# ----------------------------------- RUN TweetRead.py now -----------------------------------
ssc
# start the spark stream 
ssc.start()    
count = 0
while count < 10:
    
    time.sleep( 3 )
    top_10_tweets = sqlContext.sql( 'Select tag, count from tweets' )
    top_10_df = top_10_tweets.toPandas()
    display.clear_output(wait=True)
    count = count + 1


print ('top_10_tweets : ', top_10_tweets)
print ('spark df (top_10_tweets) : ', top_10_df)
# stop the spark stream 
ssc.stop()



