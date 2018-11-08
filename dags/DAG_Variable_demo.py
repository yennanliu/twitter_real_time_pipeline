# python3 
# ref https://www.astronomer.io/guides/airflow-datastores/
# demo pass values within differents funcs in the same DAG 

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator, BranchPythonOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.models import Variable
import datetime
import json  



args = {
'owner': 'yen',
'depends_on_past': False,
'start_date': datetime.datetime.now()}



def print_table(**kwargs):
	print ('table name : ', table)


"""

"""

sync_config = ['ABC','CDE','XYZ']


with DAG('DAG_Variable_demo', default_args=args) as dag:

	start = DummyOperator(task_id='DAG_Variable_demo')

	for table in sync_config:
		d1 =  PythonOperator(
		task_id='task__{}'.format(table),
		python_callable=print_table,	
		#pass args into python func 
		#https://airflow.readthedocs.io/en/latest/howto/operator.html	
		op_kwargs={'table': str(table)},
		provide_context=True, )


		start >> d1





