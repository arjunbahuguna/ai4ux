from pymongo import MongoClient
import numpy as np  
import pandas as pd
import sys




# Connect to MongoDB
MONGO_HOST = 'mongodb://localhost/twitterdb'
client = MongoClient(MONGO_HOST)
db = client.twitterdb
collection = db['twitter_search']
query={}
#db = _connect_mongo(host=host, port=port, username=username, password=password, db=db)

data = pd.DataFrame(list(collection.find()))



# Make a query to the specific DB and Collection
#cursor = db[collection]



# Expand the cursor and construct the DataFrame
#df =  pd.DataFrame(list(cursor))