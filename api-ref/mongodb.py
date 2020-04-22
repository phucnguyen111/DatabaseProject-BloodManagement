import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId # object id for querying account in id
import logging
import pathlib
import os
import yaml
import datetime

# constants
CLIENT = "vchainuser"
COLLECTION = "v-id"
MONGO_CLIENT = "mongodb://thaont:thaont123@178.128.217.110:27017"

logger = logging.getLogger(__name__)

myclient = MongoClient(MONGO_CLIENT)

mydb = myclient[CLIENT]
#mydb.drop_collection("v-id") # this is for testing purpose
mycol = mydb[COLLECTION]

#x = mycol.insert_one(mydict)

#print(x.inserted_id) 

collist = mydb.list_collection_names()
if "v-id" in collist:
  print("The collection exists.")

def get_user(public_key):
    query = {"public_key": public_key}
    result = mycol.find(query)

    try:
        count = 0
        response = {}
        for res in result:
            count = count + 1
            response = res # return the whole user for further uses
        if count == 1:
            return response
        else:
            return None
    except:
        return None

def create_user(info):
    res = mycol.insert_one(info)
    return res

def update_user(public_key, key, info):
    query = {"public_key": public_key}
    update = {"$set": { key: info }}
    mycol.update_one(query, update) # update a user given an id (add more field)
