import time
import os 
import pandas as pd 
from sqlalchemy import create_engine




def update2sqlite(df):
	try:
		df_ = df 
		engine = create_engine('sqlite:///twitter_data.db', echo=False)
		df_.to_sql('twitter_data',if_exists='replace',con=engine)
		print ('update to DB ok')
	except:
		print ('dump DB failed')


if __name__ == '__main__':
	df = pd.read_csv('twitter_data.csv')
	print ('load csv :')
	print (df.head())
	print ('insert csv df to sqlite....')
	update2sqlite(df)


