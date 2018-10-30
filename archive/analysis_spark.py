# python 3 

"""

* Spark reads data from S3, analyze data and save result to RDS.

modify from 
https://nycdatascience.com/blog/student-works/web-scraping/build-near-real-time-twitter-streaming-analytical-pipeline-scratch-using-spark-aws/

"""


from __future__ import print_function
import sys
import re
from operator import add
import pandas as pd
from pyspark.sql.types import StructField, StructType, StringType
from pyspark.sql import Row
from pyspark.sql.types import *
from pyspark.sql import SQLContext
import json
import boto
import boto3
from boto.s3.key import Key
import boto.s3.connection
from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
from pyspark.ml.feature import MinMaxScaler
from pyspark.ml.linalg import Vectors, VectorUDT
from pyspark.sql.functions import *
import credentials

#aws keys
aws_key_id = credentials.aws['key_id']
aws_key = credentials.aws['key']

def main():
    conf = SparkConf().setAppName("first")
    sc = SparkContext(conf=conf)
    #print 40 * '-'
    sc._jsc.hadoopConfiguration().set("fs.s3n.awsAccessKeyId",aws_key_id)
    sc._jsc.hadoopConfiguration().set("fs.s3n.awsSecretAccessKey",aws_key)
    config_dict = {"fs.s3n.awsAccessKeyId":aws_key_id,
               "fs.s3n.awsSecretAccessKey":aws_key}
    bucket = "project4capstones3"
    prefix = "/2017/07/*/*/*"
    filename = "s3n://{}/Trump/{}".format(bucket, prefix)

    rdd = sc.hadoopFile(filename,
                    'org.apache.hadoop.mapred.TextInputFormat',
                    'org.apache.hadoop.io.Text',
                    'org.apache.hadoop.io.LongWritable',
                    conf=config_dict)
    spark = SparkSession.builder.appName("PythonWordCount").config("spark.files.overwrite","true").getOrCreate()

    df = spark.read.json(rdd.map(lambda x: x[1]))
    data_rm_na = df.filter(df["status_id"]!='None')
    features_of_interest = ["rt_status_user_followers_count",\
                        'rt_status_user_friends_count',\
                        'rt_status_user_statuses_count',\
                        'rt_status_retweet_count',\
                        'rt_status_user_listed_count',\
                        'rt_status_user_id',\
                        'rt_status_created_at',\
                        'status_created_at',\
                        'rt_status_user_name',\
                        'rt_status_num_user_mentions',\
                        'searched_names',\
                        'rt_status_sentMag',\
                        'rt_status_sentScore',\
                        'rt_status_favorite_count',\
                        'status_id']

    df_reduce= data_rm_na.select(features_of_interest)
    df_reduce = df_reduce.withColumn("rt_status_user_followers_count", df_reduce["rt_status_user_followers_count"].cast(IntegerType()))
    df_reduce = df_reduce.withColumn("rt_status_user_friends_count", df_reduce["rt_status_user_friends_count"].cast(IntegerType()))
    df_reduce = df_reduce.withColumn("rt_status_user_statuses_count", df_reduce["rt_status_user_statuses_count"].cast(IntegerType()))
    df_reduce = df_reduce.withColumn("rt_status_retweet_count", df_reduce["rt_status_retweet_count"].cast(IntegerType()))
    df_reduce = df_reduce.withColumn("rt_status_user_listed_count", df_reduce["rt_status_user_listed_count"].cast(IntegerType()))
    df_reduce = df_reduce.withColumn("rt_status_favorite_count", df_reduce["rt_status_favorite_count"].cast(IntegerType()))
    df_reduce = df_reduce.withColumn("rt_status_num_user_mentions", df_reduce["rt_status_num_user_mentions"].cast(IntegerType()))


    url_ = "jdbc:mysql://twittertalker1.csjkhjjygutf.us-east-1.rds.amazonaws.com:3306/innodb"
    table_name_ = "retweet"
    mode_ = "overwrite"

    df_reduce.write.format("jdbc").option("url", url_)\
    .option("dbtable", table_name_)\
    .option("driver", "com.mysql.jdbc.Driver")\
    .option("user", "XXXXXX")\
    .option("password", "XXXXXXXX")\
    .mode(mode_)\
    .save()



if __name__ == "__main__":
    main()

