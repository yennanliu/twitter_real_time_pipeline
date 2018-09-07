# twitter_real_time_pipeline
* Dev 
* Collect twitter event data via streaming API and digest/preprocess the data 
* https://developer.twitter.com/

# Quick Start

```bash 
# run the test script 
$ git clone https://github.com/yennanliu/twitter_real_time_pipeline.git
$ cd ~ && cd twitter_real_time_pipeline
$ export APP_KEY=<your_APP_KEY> 
$ export APP_SECRET=<your_APP_SECRET>
$ python test.py 
``` 

```bash 
# run the etl script (airflow)
export AIRFLOW_HOME="$(pwd)"
# initialize db 
airflow initdb
# start the web server, default port is 8080
airflow webserver -p 8080
# start the scheduler
airflow scheduler

```


# ref 
* https://github.com/uclatommy/tweetfeels
* https://medium.com/datascape/twitter-real-time-streaming-api-use-with-python-tweet-mining-3b04a52f18d8

