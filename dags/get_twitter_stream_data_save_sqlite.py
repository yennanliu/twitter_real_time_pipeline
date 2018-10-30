"""
Code that goes along with the Airflow tutorial located at:
https://github.com/apache/incubator-airflow/blob/master/airflow/example_dags/tutorial.py

"""
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator, BranchPythonOperator
from datetime import datetime, timedelta
#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import os 

# UDF 
from utility import * 



# -----------------------------------


#Variables that contains the user credentials to access Twitter API 
# TODO : use .ymal load credentials
try:
    access_token = os.environ['access_token']
    access_token_secret = os.environ['access_token_secret']
    consumer_key = os.environ['consumer_key']
    consumer_secret = os.environ['consumer_secret']
except:
    print ('='*70)
    print (' No needed credentials , please set up  via : ')
    print (' https://developer.twitter.com/en/apps')
    print ('='*70)


# -----------------------------------
   

args = {
    'owner': 'yen',
    'depends_on_past': False,
    'start_date': datetime.now()
}



# -----------------------------------
# job func 


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (data)


def main():
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])


# -----------------------------------




dag = DAG('get_twitter_stream_data_save_sqlite', default_args=args)


get_twitter_stream_data_task = BashOperator(
    task_id='get_twitter_stream_data_part',
    bash_command = 'python /Users/yennanliu/twitter_real_time_pipeline/get_twitter_data_V2.py > twitter_data_airflow.txt',
    dag=dag
    )
save_to_db_task = PythonOperator(
    task_id='sqlite_IO',
    python_callable=update2sqlite
    )

# define workflow
#get_twitter_stream_data_task >>  save_to_db_task
get_twitter_stream_data_task










