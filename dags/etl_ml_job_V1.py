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


def main():
	boston = load_boston()
	df = pd.DataFrame(boston.data, columns=boston.feature_names)
	df['target'] = boston.target
	X = df[['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX','PTRATIO', 'B', 'LSTAT']]
	Y = np.array(df['target']).astype(int)
	regr = linear_model.LinearRegression()
	regr.fit(X, Y)
	print (pd.DataFrame({'predict':regr.predict(X), 'actual':Y, 'error':Y - regr.predict(X)}))
	print ('score :', regr.score(X,Y))
	print ('intercept_ : ' , regr.fit(X, Y).intercept_, '\n', 'coef_ : ', regr.fit(X, Y).coef_)


# -----------------------------------


with DAG('etl_ml_job_V1', default_args=args) as dag:
    ML_train_step_1 = PythonOperator(
        task_id='main',
        python_callable=main
        )

    # define workflow
    ML_train_step_1  





