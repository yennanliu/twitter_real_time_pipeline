# python3 
# Dynamically Generating DAGs in Airflow
# https://www.astronomer.io/guides/dynamically-generating-dags/

from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator



def create_dag(dag_id,
               schedule,
               dag_number,
               default_args):

    def hello_world_py(*args):
        print('Hello World')
        print('This is DAG: {}'.format(str(dag_number)))

    dag = DAG(dag_id,
              schedule_interval=schedule,
              default_args=default_args)

    with dag:
        t1 = PythonOperator(
            task_id='hello_world',
            python_callable=hello_world_py,
            dag_number=dag_number)

    return dag


# build a dag for each number in range(10)
for n in range(1, 10):
    dag_id = 'Dag_dynamic_generate_DAG_demo_HELLOWORLD_{}'.format(str(n))

    args = {'owner': 'yen',
            'start_date': datetime(2018, 1, 1)}

    schedule = '@daily'

    dag_number = n

    globals()[dag_id] = create_dag(dag_id,
                                  schedule,
                                  dag_number,
                                  args)

