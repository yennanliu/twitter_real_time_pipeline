# python3 
# Templating and Macros in Airflow
# https://www.astronomer.io/guides/templating/

# airflow Macros ref 
# https://airflow.apache.org/code.html#macros


from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2018, 5, 26),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


def test(**kwargs):

    first_date = kwargs.get('execution_date', None)
    next_execution_date = '{{ next_execution_date }}'

    print("NEXT EXECUTION DATE {0}".format(next_execution_date))
    print("EXECUTION DATE: {0}".format(first_date))


with DAG(dag_id='DAG_templates_macros_demo', default_args=default_args,schedule_interval='@once') as dag:
    execution_date = '{{ execution_date }}'
    t1 = PythonOperator(
        task_id='DAG_templates_macros_demo',
        python_callable=test,
        template_dict={'execution_date': execution_date},
        provide_context=True)
