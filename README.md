# twitter_real_time_pipeline


<img src ="https://github.com/yennanliu/twitter_real_time_pipeline/blob/master/ref/twitter_pipeline.png">



* Collect twitter event data via streaming API and digest/preprocess the data 
* https://developer.twitter.com/

# Tech
* ETL 
	- Python3, Airflow, Pyspark tweepy ,twython, 
* DL 
	- Keras, Tensorflow 
* DB
	- SQLite, Bigquery  
* Others 
	- Cloud Pub/Sub, Cloud storage 

# Architecture
``` 
# 1) Local 
python script call Twitter real-time API -> save as txt/Sqlite -> python script read txt/sqlite data as dataframe -> trained RNN emojify model predict with new updated streaming data -> output prediction : response emoji corresponding to twitter message e.g. : input : she said yes |  prediction: she said yes 😄


# 2) Cloud 
# dev 

```


# Quick Start

### Local (batch)

```bash 
# ----------- Run the test script (BATCH) ----------- # 
$ git clone https://github.com/yennanliu/twitter_real_time_pipeline.git
$ cd ~ && cd twitter_real_time_pipeline
# get the APP_KEY, APP_SECRET  here :  https://developer.twitter.com/
#$ export APP_KEY=<your_APP_KEY> 
#$ export APP_SECRET=<your_APP_SECRET>
$ nano .creds.yml # update .creds.yml with your consumer_key,  consumer_secret
# batch 
$ python get_twitter_data_V1

```

### Local (Stream)

```bash 
# ----------- Run the test script  (STREAM) ----------- # 
$ git clone https://github.com/yennanliu/twitter_real_time_pipeline.git
$ cd ~ && cd twitter_real_time_pipeline
# get the APP_KEY, APP_SECRET  here :  https://developer.twitter.com/
#export access_token=<access_token>  && export access_token_secret=<access_token_secret>  && export consumer_key=<your_APP_KEY>   && export consumer_secret=<your_APP_SECRET>
$ nano .creds.yml # update .creds.yml with your access_token, access_token_secret....
# save to txt 
$ python get_twitter_data_V2.py  > twitter_data.txt 
# open the other terminal and run the following python script 
$ python twitter_data_to_df.py && python twitter_data_to_sqlite.py

####### output  #######
======================================================================
 twitter df : 
======================================================================
                                                  text lang  \
0    Stets' eyes widen as he realizes the ship is o...   en   
1    RT @eunice_atuejide: Nnamdi Kalu is a deceitfu...   en   
2    @bubbyjaney If 'marshmallow version of Harley ...   en   
3    rubyのメソッド、調べて勉強φ(..)！(ver2.5.0)\nClass  : Nume...   ja   
4    RT @_Nslhnc: Reims c'est vraiment un autre mon...   fr   
5    Ça chauffe entre Ruby et Jackson. Ils vont pre...   fr   
6    RT @Transfanman: Ruby Navarro https://t.co/yr3...   ht   
7    My dogs name is Ruby. \nI call her:\nRoobs \nR...   en   
8                                  Don't mind the fool   en   
9    DAY10\n40分\n\n・JavaScript 学習コース Ⅲ 関数と引数のところだけ\...   ja   
...
                                              source country  
0  <a href="http://twitter.com/download/iphone" r...     NaN  
1  <a href="http://twitter.com/download/android" ...     NaN  
2  <a href="http://www.babynames.com" rel="nofoll...     NaN  
3  <a href="https://mobile.twitter.com" rel="nofo...     NaN  
4  <a href="https://mobile.twitter.com" rel="nofo...     NaN  
insert csv df to sqlite....
update to DB ok


``` 

### Local (Aifflow, Batch)
```bash 
# ----------- Run via etl script (airflow)----------- # 
$ git clone https://github.com/yennanliu/twitter_real_time_pipeline.git
$ export APP_KEY=<your_APP_KEY> 
$ export APP_SECRET=<your_APP_SECRET>
$ cd ~ && cd twitter_real_time_pipeline
# set up airflow route 
$ export AIRFLOW_HOME="$(pwd)"
# set up python route 
$ export PYTHONPATH=$(pwd) 
# modify airflow cfg (not show example DAG at UI)
# nano unittests.cfg  -> load_examples = False 

# initialize db 
$ airflow initdb
### make sure all jobs files under /dags are without syntax errors ### 

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














