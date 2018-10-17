"""
Code that goes along with the Airflow tutorial located at:
https://github.com/apache/incubator-airflow/blob/master/airflow/example_dags/tutorial.py
"""
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator, BranchPythonOperator
from datetime import datetime, timedelta

# UDF 
from utility import * 


args = {
    'owner': 'yen',
    'depends_on_past': False,
    'start_date': datetime.now()
}


# -----------------------------------
# job func 

# -----------------------------------




with DAG('etl_job_V3', default_args=args) as dag:
    get_twitter_data_task = PythonOperator(
        task_id='main',
        python_callable=main
        )
    save_to_db_task = PythonOperator(
        task_id='sqlite_IO',
        python_callable=update2sqlite
        )

    # define workflow
    get_twitter_data_task >>  save_to_db_task










