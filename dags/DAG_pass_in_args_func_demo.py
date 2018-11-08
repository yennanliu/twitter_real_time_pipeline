# python 3 
# Passing in arguments
# https://airflow.readthedocs.io/en/latest/howto/operator.html
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
import datetime
import time 


args = {
'owner': 'yen',
'depends_on_past': False,
'start_date': datetime.datetime.now()}




def my_sleeping_function(random_base):
    """This is a function that will run within the DAG execution"""
    print (' random_base : ',  random_base)
    time.sleep(random_base)



with DAG('DAG_pass_in_args_func_demo', default_args=args) as dag:
	run_this = DummyOperator(task_id='run_this')
	# Generate 10 sleeping tasks, sleeping from 0 to 4 seconds respectively
	for i in range(5):
		task = PythonOperator(
		    task_id='sleep_for_' + str(i),
		    python_callable=my_sleeping_function,
		    op_kwargs={'random_base': float(i) / 10},
		    dag=dag,
		)

		run_this >> task



