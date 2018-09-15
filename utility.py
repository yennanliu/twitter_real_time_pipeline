# python 3 


from twython import Twython
import time
import os 
import pandas as pd 

try:
    APP_KEY = os.environ['APP_KEY']
    APP_SECRET = os.environ['APP_SECRET'] 
except:
    print (' No API key , please set up  via : ')
    print (' https://developer.twitter.com/en/apps')


# -----------------------------------------
# op func 



def main():
    twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
    ACCESS_TOKEN = twitter.obtain_access_token()
    print (ACCESS_TOKEN)          
    ACCESS_TOKEN = ACCESS_TOKEN
    twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
    twitter.get_application_rate_limit_status()['resources']['search']
    #RETRIEVING REAL TIME STREAMING TWEETS ABOUT BLOCKCHAIN 
    search = twitter.search(q="blockchain", count=2000)
    tweets = search['statuses']
    #for tweet in tweets:
    #print (tweet['id_str'], '\n', tweet['text'], tweet['favorite_count'], tweet['retweet_count'] ), '\n\n\n'
    ids = []
    #for tweet in tweets:
    #ids.append(tweet['id_str'])
    ids = [tweet['id_str'] for tweet in tweets]
    texts = [tweet['text'] for tweet in tweets]
    times = [tweet['retweet_count'] for tweet in tweets]
    favtimes = [tweet['favorite_count'] for tweet in tweets]
    follower_count = [tweet['user']['followers_count'] for tweet in tweets]
    location = [tweet['user']['location'] for tweet in tweets]
    lang = [tweet['lang'] for tweet in tweets]
    #print (tweets[0])
    df = pd.DataFrame(tweets)
    print (df.head(5))
    return df 



# -----------------------------------------


def update2sqlite():
	try:
		df = main()
		df.to_sql('twitter_data',if_exists='append',con='sqlite:///twitter.db')
		print ('update to DB ok')
	except:
		print ('dump DB failed')



class sqlite_IO:
	def __init__(self, *args, **kwargs):
		self.df = main()
		self.con  = 'sqlite:///twitter.db'

	def test(self):
		print (self.con)

	def dumb2db(self):
		try:
			df = self.df 
			df.to_sql('twitter_data',if_exists='append',con=self.con)
			print ('update to DB ok')
		except:
			print ('dump DB failed')


# -----------------------------------------


