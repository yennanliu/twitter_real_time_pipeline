# python3 
# airflow managing-dependencies
# https://www.astronomer.io/guides/managing-dependencies/

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator, BranchPythonOperator
from airflow.hooks.postgres_hook import PostgresHook
from datetime import datetime, timedelta, time
import numpy as np 

args = {
'owner': 'yen',
'depends_on_past': False,
'start_date': datetime(2018,11,6),
'retries': 1,
'retry_delay': timedelta(minutes=1)}



def python_func_demo():
	print ('this is python_func_demo')



with DAG(dag_id='DAG_manage_dependencies_demo', default_args=args) as dag:

	d1 = DummyOperator(task_id='d1')

	branch = BranchPythonOperator(task_id='python_func_demo', python_callable=python_func_demo)

	d2 = DummyOperator(task_id='d2')
	d3 = DummyOperator(task_id='d3')
	d4 = DummyOperator(task_id='d4')



	# Set the dependencies 
	d1 >> branch
	branch >> d2 >> (d3, d4) 
	branch >> [d3, d4]


