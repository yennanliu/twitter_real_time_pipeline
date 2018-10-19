# python 3 
# modify from http://adilmoujahid.com/posts/2014/07/twitter-analytics/


#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import os 


#Variables that contains the user credentials to access Twitter API 
# TODO : use .ymal load credentials
try:
    access_token = os.environ['access_token']
    access_token_secret = os.environ['access_token_secret']
    consumer_key = os.environ['consumer_key']
    consumer_secret = os.environ['consumer_secret']
except:
    print ('='*70)
    print (' No needed credentials , please set up  via : ')
    print (' https://developer.twitter.com/en/apps')
    print ('='*70)



#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (data)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])