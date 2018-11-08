# python3 
# ref https://www.astronomer.io/guides/airflow-datastores/
# demo pass values within differents funcs in the same DAG 

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator, BranchPythonOperator
import datetime 



args = {
    'owner': 'yen',
    'depends_on_past': False,
    'start_date': datetime.datetime.now()}


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


sync_config = json.loads(Variable.get("sync_config"))

with dag:

    start = DummyOperator(task_id='Variable_demo_DAG')

    for table in sync_config:
        d1 = RedshiftToS3Transfer(
            task_id='{0}'.format(table['s3_key']),
            table=table['table'],
            schema=table['schema'],
            s3_bucket=table['s3_bucket'],
            s3_key=table['s3_key'],
            redshift_conn_id=table['redshift_conn_id']
        )
        start >> d1
















