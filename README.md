# twitter_real_time_pipeline

* Collect twitter event data via streaming API and digest/preprocess the data 
* https://developer.twitter.com/

# Quick Start

```bash 
# run the test script 
$ git clone https://github.com/yennanliu/twitter_real_time_pipeline.git
$ cd ~ && cd twitter_real_time_pipeline
# get the APP_KEY, APP_SECRET  here :  https://developer.twitter.com/
$ export APP_KEY=<your_APP_KEY> 
$ export APP_SECRET=<your_APP_SECRET>
$ python test.py 
``` 

```bash 
# run the etl script (airflow)
export AIRFLOW_HOME="$(pwd)"
# initialize db 
airflow initdb
### make sure all jobs files under /dags are without syntax errors ### 
# not load example dags 
export load_examples=False
# fix  ValueError: unknown locale: UTF-8 in Python (mac OSX)
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
# start the web server, default port is 8080
airflow webserver -p 8080
# start the scheduler
airflow scheduler

```


# ref 
* https://github.com/uclatommy/tweetfeels
* https://medium.com/datascape/twitter-real-time-streaming-api-use-with-python-tweet-mining-3b04a52f18d8

