#!/usr/bin/env bash


#source activate pyspark_
export SLUGIFY_USES_TEXT_UNIDECODE=yes
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export AIRFLOW_HOME=$(PWD)
export PYTHONPATH=$(pwd)

echo 'APP_KEY = '  $APP_KEY
echo 'APP_SECRET = '  $APP_SECRET

#export APP_KEY=<APP_KEY> 
#export APP_SECRET=<APP_SECRET> 
