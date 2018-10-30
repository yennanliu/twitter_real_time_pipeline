# python 3 

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator, BranchPythonOperator
from datetime import datetime, timedelta
import os 



args = {
    'owner': 'yen',
    'depends_on_past': False,
    'start_date': datetime.now()
}

#dag = DAG('etl_app_V3', default_args=args)



# -----------------------------------
# job func 

def main():
	from pyspark import SparkConf, SparkContext
	from pyspark.sql import SQLContext
	conf = SparkConf().setAppName("building a warehouse")
	sc = SparkContext(conf=conf)
	sqlCtx = SQLContext(sc)
	#spark_home = os.environ.get('SPARK_HOME', None)
	spark_home='/Users/yennanliu/spark'
	print ('spark_home : ', spark_home)
	text_file = sc.textFile(spark_home + "/README.md")
	word_counts = text_file \
	.flatMap(lambda line: line.split()) \
	.map(lambda word: (word, 1)) \
	.reduceByKey(lambda a, b: a + b)
	word_counts.collect()
	print (word_counts.collect())



# -----------------------------------



with DAG('etl_spark_job_V1', default_args=args) as dag:

    #launch_spark_env_task = BashOperator(
    #	task_id = 'launch_spark_env_task',
    #	bash_command = 'source activate pyspark_ && export SPARK_HOME=/Users/yennanliu/spark && export PATH=$SPARK_HOME/bin:$PATH'
    #)
    spark_task = PythonOperator(
        task_id='spark_task',
        python_callable=main
    )
    #launch_spark_env_task >> spark_task
    #launch_spark_env_task >> spark_task
    spark_task



