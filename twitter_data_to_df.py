# python 3 
# http://adilmoujahid.com/posts/2014/07/twitter-analytics/

import json 
import re 
import pandas as pd 


def fix_text(x):
    """

    remove  ‘@’mention
    https://towardsdatascience.com/another-twitter-sentiment-analysis-bb5b01ebad90
    
    """
    try :
        # remove ' @_userid: ' 
        return x.split(':')[1].strip(' ')
    except:
        # remove ‘@’mention
        return re.sub(r'@[A-Za-z0-9]+','',x).strip(' ')
        # return anything else 
    else:
        return x 



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
# fix text 
tweets['text'] =  tweets['text'].apply(fix_text)
print ('='*70)
print (' twitter df : ')
print ('='*70)
print (tweets)
print ('save to csv...')
tweets.to_csv('twitter_data.csv')





