# python 3


# AIRFLOW
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator, BranchPythonOperator
from datetime import datetime, timedelta
# OP 
from sklearn.datasets import load_boston
import pandas as pd, numpy as np
# ML 
from sklearn import datasets, linear_model




# -----------------------------------
# config job 


args = {
    'owner': 'yen',
    'depends_on_past': False,
    'start_date': datetime.now()}

# -----------------------------------




# -----------------------------------
# job func 


def train_V1():
	boston = load_boston()
	df = pd.DataFrame(boston.data, columns=boston.feature_names)
	df['target'] = boston.target
	X = df[['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX','PTRATIO', 'B', 'LSTAT']]
	Y = np.array(df['target']).astype(int)
	regr = linear_model.LinearRegression()
	regr.fit(X, Y)
	prdiction = pd.DataFrame({'predict':regr.predict(X), 'actual':Y, 'error':Y - regr.predict(X)})
	print (pd.DataFrame({'predict':regr.predict(X), 'actual':Y, 'error':Y - regr.predict(X)}))
	print ('score :', regr.score(X,Y))
	print ('intercept_ : ' , regr.fit(X, Y).intercept_, '\n', 'coef_ : ', regr.fit(X, Y).coef_)
	return prdiction


def train_V2():
	boston = load_boston()
	df = pd.DataFrame(boston.data, columns=boston.feature_names)
	df['target'] = boston.target
	X = df[['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX','PTRATIO', 'B', 'LSTAT']]
	Y = np.array(df['target']).astype(int)
	regr = linear_model.LinearRegression()
	regr.fit(X, Y)
	prdiction = pd.DataFrame({'predict':regr.predict(X), 'actual':Y, 'error':Y - regr.predict(X)})
	print (pd.DataFrame({'predict':regr.predict(X), 'actual':Y, 'error':Y - regr.predict(X)}))
	print ('score :', regr.score(X,Y))
	print ('intercept_ : ' , regr.fit(X, Y).intercept_, '\n', 'coef_ : ', regr.fit(X, Y).coef_)
	return prdiction 


def save_output(**context):
	print ('context : ', context)
	context_ = context.xcom_pull(task_ids='ML_train_step_1')
	pd.DataFrame(context_).to_csv('etl_ml_job_V2_output.csv')


# -----------------------------------


with DAG('etl_ml_job_V2', default_args=args) as dag:
    ML_train_step_1 = PythonOperator(
        task_id='train_V1',
        python_callable=train_V1
        #provide_context=True
        )

    ML_train_step_2 = PythonOperator(
        task_id='train_V2',
        python_callable=train_V2
        #provide_context=True 
        )

    save_output_task = PythonOperator(
        task_id='save_output',
        python_callable=save_output
        #source_objects=["{{ task_instance.xcom_pull(task_ids='ML_train_step_1') }}"]
        )


    # define workflow
    ML_train_step_1 >> save_output_task
    ML_train_step_2 >> save_output_task






