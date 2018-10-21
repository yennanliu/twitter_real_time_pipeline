# python 3 
# http://adilmoujahid.com/posts/2014/07/twitter-analytics/

import pandas as pd 
import json 


tweets_data_path = 'twitter_data.txt'
tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:      
        tweet = json.loads(line)
        tweets_data.append(tweet)
        print (' load file OK ')
    except:
        print (' sth wrong')
        continue
print (len(tweets_data))
tweets = pd.DataFrame()
tweets['text'] = list(map(lambda tweet: tweet['text'], tweets_data))
tweets['lang'] = list(map(lambda tweet: tweet['lang'], tweets_data))
tweets['created_at'] = list(map(lambda tweet: tweet['created_at'], tweets_data))
tweets['geo'] = list(map(lambda tweet: tweet['geo'], tweets_data))
tweets['source'] = list(map(lambda tweet: tweet['source'], tweets_data))
tweets['country'] = list(map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data))
print ('='*70)
print (' twitter df : ')
print ('='*70)
print (tweets)
print ('save to csv...')
tweets.to_csv('twitter_data.csv')





