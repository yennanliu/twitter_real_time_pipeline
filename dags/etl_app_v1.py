# python 3 


import time
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2100, 1, 1, 0, 0),
    'schedule_interval': '@daily',
    'retries': 2,
    'retry_delay': timedelta(minutes=1)
}



def main_V1():
    print ('start running test.py (twitter API scrapper)....')
    error_happen = time.time() % 2 > 1
    if error_happen:
        print (' sth weird happen, etl jobs failed')
        return
    api_available = time.time() % 2 > 1
    if api_available:
        print (' ok, run the etl job')
        print (' update real-time twitter data')
    else:
        print (' no-need to update, no etl job been executed')



with DAG('etl_app_v1', default_args=default_args) as dag:
    superman_task = PythonOperator(
        task_id='etl_V1_task',
        python_callable=main_V1
    )


