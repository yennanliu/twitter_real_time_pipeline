#!/usr/bin/python
# -*- coding: utf-8 -*-
# python3
# airflow managing-dependencies
# https://www.astronomer.io/guides/managing-dependencies/

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator, \
    BranchPythonOperator
from airflow.utils.trigger_rule import TriggerRule
from datetime import datetime, timedelta, time
import numpy as np

args = {
    'owner': 'yen',
    'depends_on_past': False,
    'start_date': datetime(2018, 11, 6),
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
    }


def python_func_demo():
    print ('this is python_func_demo')


# Define some failure handling

def fail_logic(**kwargs):

    # Implement fail_logic here.

    return 'sth failed'


with DAG(dag_id='DAG_manage_dependencies_demo', default_args=args) as \
    dag:

    # d1 = DummyOperator(task_id='d1')
    # branch = BranchPythonOperator(task_id='python_func_demo', python_callable=python_func_demo)
    # d2 = DummyOperator(task_id='d2')
    # d3 = DummyOperator(task_id='d3')
    # d4 = DummyOperator(task_id='d4')

    # Set the dependencies
    # d1 >> branch
    # Both of these are equivalent, and set d3 and d4 downstream of d2.
    # i.e. d2 >> (d3, d4)  is as same as  d2 >> [d3, d4]
    # branch >> d2 >> (d3, d4)
    # branch  >> [d3, d4]

    job_info = [{'job_name': 'train_model', 'brittle': True},
                {'job_name': 'execute_query', 'brittle': False}]

    for job in job_info:
        d5 = DummyOperator(task_id=job['job_name'])

        # Generate a task based on a condition

        if job['brittle']:
            d6 = PythonOperator(task_id='{0}_{1}'.format(job['job_name'
                                ], 'fail_logic'),
                                python_callable=fail_logic,
                                provide_context=True,
                                trigger_rule=TriggerRule.ONE_FAILED)
            d5 >> d6
        for i in range(0, 5):
            downstream = \
                DummyOperator(task_id='{0}_{1}'.format(job['job_name'],
                              i))

            d5 >> downstream


			