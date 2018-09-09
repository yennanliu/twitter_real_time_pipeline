#!/usr/bin/env bash


# steps 
# step 1) 
# https://airflow.apache.org/start.html#quick-start
export AIRFLOW_HOME=~/airflow

# step 2)  
# config 
# https://github.com/un33k/python-slugify/issues/52
export SLUGIFY_USES_TEXT_UNIDECODE=yes
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
# step 3) 
# install from pypi using pip
pip install apache-airflow
pip install "apache-airflow[crypto, slack]"
# step 4) 
# initialize the database
airflow initdb

# step 5) 
# start the web server, default port is 8080
airflow webserver -p 8080

# step 6) 
# start the scheduler
airflow scheduler
