from pymongo import MongoClient
import numpy as np  
import pandas
import sys

MONGO_HOST = 'mongodb://localhost/twitterdb'

client = MongoClient(MONGO_HOST)
db = client.twitterdb
collection = db['twitter_search']

#d = dict((db, [collection for collection in client[db].list_collection_names()]) for db in client.list_database_names())


cursor=collection.find()
docs=list(cursor)
docs=docs[:25]

#use pandas.series() to convert it to Series format
#Series_obj=pandas.Series({“one”:”index”})
#Series_obj.index=[“one”]
#Print(“index”:series_obj.index) 

#create pandas dataframe object
docus=pandas.Dataframe(colums=[])


#Enumeration & Appending The Series Object
for n,doc in enumerate(docs):
    doc[“_id”]=str(doc[“_id”])
    doc_id=doc[“_id”]
series_obj=pandas.Series(doc,name=doc_id)// Series Object Creation.
docs=docs.append(series_obj)

#Using .to_json() Function
json_export = docs.to_json() # return JSON data
print ("nJSON data:", json_export)



#open file
#original_stdout = sys.stdout 
#with open('filename.txt', 'w') as f:
#	sys.stdout = f

	#write to file
#	cursor = collection.find({})
#	for document in cursor:
#         	 print(document)

#close file
#sys.stdout = original_stdout


#query specifically
