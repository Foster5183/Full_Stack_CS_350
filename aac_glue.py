# -*- coding: utf-8 -*-
# aac_glue class.py
"""
Eric L Foster 
03/25/2025
A class based OOP for interacting with our mongoDB AAC database
this class is for accessing the user account and perfoming CRUD
operations. 
"""
# __import__
import sys
import os
from pymongo import MongoClient
from bson.objectid import ObjectId

# __Class Definition__
class AnimalShelter(object):
    """AAC MongoDB CRUD Operations"""
    
    def __init__(self, username, password):
        # Connection Variables
        
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31336
        DB = 'AAC'
        COL = 'animals'
        # INIT connection
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (username,password,HOST,PORT))
        self.database = self.client[DB]
        self.collection = self.database[COL]
    #The Create in CRUD
    def create(self,data):
        if data:
            result = self.database.animals.insert_one(data)
            return result.acknowledged
        else:
            raise Exception("No Data Provided")
            return False
    #The Read in CRUD
    def read(self, query={}):
        try:
            cursor = self.collection.find(query)
            docs = []
            for doc in cursor:
                doc["_id"] = str(doc["_id"])  # Convert ObjectId to string
                docs.append(doc)
            return docs
        except Exception as e:
            print("READ ERROR:", e)
            return []
    #The Update in CRUD
    def update(self, key, value, new_data):
        if key and value and new_data:
            query = {key: value}
            result = self.collection.update_one(query,{'$set': new_data})
            return result.modified_count
        else:
            raise Exception("Values not formatted correctly")
    #The Delete in Crud 
    def delete(self, key, value): 
        if key and value:
            query = {key: value}
            result = self.collection.delete_one(query)
            return result.deleted_count
        else:
            raise Exception("Values not formatted correctly")