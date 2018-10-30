# python 3 
import yaml
import os

with open('.creds.yml') as f:
    config = yaml.load(f)

access_token = config['twitter_api']['access_token']
access_token_secret = config['twitter_api']['access_token_secret'] 
consumer_key = config['twitter_api']['consumer_key']
consumer_secret = config['twitter_api']['consumer_secret'] 
APP_KEY = config['twitter_api']['APP_KEY']
APP_SECRET = config['twitter_api']['APP_SECRET'] 


def get_spotify_client_id_secret():
	print (' access_token = ', access_token)
	print (' access_token_secret = ', access_token_secret)
	print (' consumer_key = ', consumer_key)
	print (' consumer_secret = ', consumer_secret)
	print (' APP_KEY = ', APP_KEY)
	print (' APP_SECRET = ', APP_SECRET)
	return access_token, access_token_secret, consumer_key, consumer_secret, APP_KEY, APP_SECRET