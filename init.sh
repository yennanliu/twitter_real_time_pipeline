#!/usr/bin/env bash


#source activate pyspark_
export SLUGIFY_USES_TEXT_UNIDECODE=yes
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export AIRFLOW_HOME=$(PWD)
export PYTHONPATH=$(pwd)



#### TODO : airflow quick start : initDB, launch UI, launch scheduler ####

#airflow initdb
#export load_examples=False
#airflow webserver -p 8080
#airflow scheduler