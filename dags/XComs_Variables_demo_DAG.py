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


def generate_values(**kwargs):
    values = list(range(0, 100))
    return values


def manipulate_values(**kwargs):
    ti = kwargs['ti']
    v1 = ti.xcom_pull(key=None, task_ids='push_values')
    print ('v1 (from xcom_pull  ) : ', v1 )

    return [x / 2 for x in v1]


with DAG('XComs_Variables_demo_DAG', default_args=args) as dag:

    t1 = PythonOperator(
        task_id='push_values',
        python_callable=generate_values,
        provide_context=True)

    t2 = PythonOperator(
        task_id='pull_values',
        python_callable=manipulate_values,
        provide_context=True)

    t1 >> t2 







