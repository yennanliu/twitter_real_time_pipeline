# python 3 
# Passing in arguments
# https://www.astronomer.io/guides/airflow-branch-operator/ 


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





def get_recent_date2():
	random_val = np.random.randint(2, size=1)[0]

	if random_val != 0:
		print ('random_val == 1')
		return 'trigger_warning'
	return 'kickoff_summary_tables'



#def check_for_data():
#	print (' -------- check for data --------  ') 


with DAG(dag_id='DAG_BranchOperator_demo', default_args=args) as dag:
	kick_off_dag = DummyOperator(task_id='kick_off_dag')

	branch = BranchPythonOperator(task_id='check_for_data', python_callable=get_recent_date2)

	kickoff_summary = DummyOperator(task_id='kickoff_summary_tables')

	# Replace this with the type of warning you want to trigger.
	# I.e. slack notification, trigger DAG, etc.
	trigger_warning = DummyOperator(task_id='trigger_warning')

	run_condition = DummyOperator(task_id = 'sql_statement_one')
	downstream_task = DummyOperator(task_id = 'sql_statement_two')

	# Set the dependencies for both possibilities
	kick_off_dag >> branch
	branch >> kickoff_summary >> run_condition >> downstream_task
	branch >> trigger_warning



