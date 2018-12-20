################################################################################################
#
#
#
# ref 
# https://www.udemy.com/join/login-popup/?next=/spark-and-python-for-big-data-with-pyspark/learn/v4/t/lecture/7047216%3Fstart%3D570
#
#
#
################################################################################################

# op 
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import socket
import json
import os 
# UDF 
from load_creds import * 


#----------------------------------------------------
# config 

try:
    access_token, access_token_secret, consumer_key, consumer_secret = get_twitter_api_secret() 
    APP_KEY=consumer_key
    APP_SECRET=consumer_secret

except:
    access_token = os.environ['access_token']
    access_token_secret = os.environ['access_token_secret']
    consumer_key = os.environ['consumer_key']
    consumer_secret = os.environ['consumer_secret'] 
else:
    print (' No API key , please set up  via : ')
    print (' https://developer.twitter.com/en/apps')


#----------------------------------------------------


class TweetsListener(StreamListener):

  def __init__(self, csocket):
      self.client_socket = csocket

  def on_data(self, data):
      try:
          msg = json.loads( data )
          print( msg['text'].encode('utf-8') )
          self.client_socket.send( msg['text'].encode('utf-8') )
          return True
      except BaseException as e:
          print("Error on_data: %s" % str(e))
      return True

  def on_error(self, status):
      print(status)
      return True

def sendData(c_socket):
  auth = OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_secret)

  twitter_stream = Stream(auth, TweetsListener(c_socket))
  twitter_stream.filter(track=['soccer'])

if __name__ == "__main__":
  s = socket.socket()         # Create a socket object
  host = "127.0.0.1"     # Get local machine name
  port = 9999                 # Reserve a port for your service.
  s.bind((host, port))        # Bind to the port

  print("Listening on port: %s" % str(port))

  s.listen(5)                 # Now wait for client connection.
  c, addr = s.accept()        # Establish connection with client.

  print( "Received request from: " + str( addr ) )

  sendData( c )