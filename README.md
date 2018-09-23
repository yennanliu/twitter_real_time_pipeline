# twitter_real_time_pipeline

* Collect twitter event data via streaming API and digest/preprocess the data 
* https://developer.twitter.com/

# Tech
* Python3, Airflow, Pyspark, twython 
* SQLite 


# Quick Start

```bash 
# ----------- Run the test script  ----------- # 
$ git clone https://github.com/yennanliu/twitter_real_time_pipeline.git
$ cd ~ && cd twitter_real_time_pipeline
# get the APP_KEY, APP_SECRET  here :  https://developer.twitter.com/
$ export APP_KEY=<your_APP_KEY> 
$ export APP_SECRET=<your_APP_SECRET>
$ python test.py 
``` 

```bash 
# ----------- Run via etl script (airflow)----------- # 
# set up airflow route 
$ export AIRFLOW_HOME="$(pwd)"
# set up python route 
$ export PYTHONPATH=$(pwd) 
# initialize db 
$ airflow initdb
### make sure all jobs files under /dags are without syntax errors ### 
# not load example dags 
$ export load_examples=False
# fix  ValueError: unknown locale: UTF-8 in Python (mac OSX)
$ export LC_ALL=en_US.UTF-8
$ export LANG=en_US.UTF-8
# start the web server, default port is 8080 (run this in 1 terminal)
$ airflow webserver -p 8080
# start the scheduler (run this in another terminal)
$ airflow scheduler

# the airflow admin UI should be available at 
# http://localhost:8080/admin/

```


# ref 
- Twitter API query 
	* https://github.com/uclatommy/tweetfeels
	* https://medium.com/datascape/twitter-real-time-streaming-api-use-with-python-tweet-mining-3b04a52f18d8
- Real-time streaming 
	* https://nycdatascience.com/blog/student-works/web-scraping/build-near-real-time-twitter-streaming-analytical-pipeline-scratch-using-spark-aws/
	* https://www.datareply.co.uk/blog/2018/5/23/realtime-streaming-data-pipeline-using-google-cloud-platform-and-bokeh
	* https://github.com/nabeeltariq2/Real-Time-Twitter-AWS-Python
	* https://www.dataquest.io/blog/streaming-data-python/
- Python Spark streaming 
	* https://www.rittmanmead.com/blog/2017/01/getting-started-with-spark-streaming-with-python-and-kafka/
	* https://medium.com/@kass09/spark-streaming-kafka-in-python-a-test-on-local-machine-edd47814746
	* https://spark.apache.org/docs/2.2.0/streaming-programming-guide.html














