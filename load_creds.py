# python 3 
import yaml
import os

with open('.creds.yml') as f:
    config = yaml.load(f)

access_token = config['twitter_api']['access_token']
access_token_secret = config['twitter_api']['access_token_secret'] 
consumer_key = config['twitter_api']['consumer_key']
consumer_secret = config['twitter_api']['consumer_secret'] 


def get_twitter_api_secret():
	print (' access_token = ', access_token)
	print (' access_token_secret = ', access_token_secret)
	print (' consumer_key = ', consumer_key)
	print (' consumer_secret = ', consumer_secret)
	return access_token, access_token_secret, consumer_key, consumer_secret