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

define the variable at UI : 

step 1) visit UI for example  : http://localhost:3333/admin/variable/ 
step 2) 
sync_config = 

[{
  "table": "users",
  "schema":"app_one",
 "s3_bucket":"etl_bucket",
 "s3_key":"app_one_users",
 "redshift_conn_id":"postgres_default" },
 {
   "table": "users",
   "schema":"app_two",
 "s3_bucket":"etl_bucket",
 "s3_key":"app_two_users",
 "redshift_conn_id":"postgres_default"}]



"""

sync_config = ['ABC','CDE','XYZ']
#sync_config = Variable.get("sync_config")




with DAG('Variable_demo_DAG', default_args=args) as dag:

	start = DummyOperator(task_id='Variable_demo_DAG')

	for table in sync_config:
		d1 =  PythonOperator(
		task_id='task__{}'.format(table),
		python_callable=print_table,
		provide_context=True)


		start >> d1
















