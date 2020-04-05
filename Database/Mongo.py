# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 21:58:02 2020

@author: Ratan Singh
"""

from pymongo import MongoClient
import logging
from datetime import datetime
import pandas as pd
from Database.Database import Database
from ConfigParser.ConfigParser import ConfigurationParser


class Mongo(Database):
    
    def __init__(self):
        
        # Instating Logger
        logging.basicConfig(filename="logs/database.log", filemode='w', level=logging.DEBUG)    

        # Database server configurations
        self.__host = "localhost"
        self.__port = 27017
        self.__maxDelay = 10
        self.__connect()
    



    """
    Database server connection code
    """
    def __connect(self):
        try:
            self.__client = MongoClient(self.__host , self.__port, serverSelectionTimeoutMS = self.__maxDelay)
            self.__client.server_info()
            logging.info("[{}] : Successfully connected to database server at {}".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), self.__host + str(self.__port)))
            logging.info("=="*30)
        except: 
            logging.error("[{}] : Could not connect to database server. Database connection is down.".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
            raise ConnectionError("Could not connect to database server. Database connection is down.")
            
            
            
#-------------------------------------------------------------------------------------------    
    """
    Selection of a Database
    """
    def getDB(self, db):
        try:
            return self.__client[db]
        except:
            logging.error("[{}] : Cannot find / create database {}".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"),db))
            raise ValueError("Error finding / creating database {}".format(db))
    
    


    """
    Returns list of all available DBs
    """
    def getAllDB(self):
        return self.__client.list_database_names()
    
    



    """
    Get a collection
    """
    def getCollection(self,dbName,collectionName):
        try:
            db = self.getDB(dbName)
            collection = db[collectionName]
            return collection
        except:
            logging.error("[{}] : Cannot find / create collection {}".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"),collectionName))
            raise ValueError("Error finding / creating collection {}".format(collectionName))
       
    




    """
    Returns list of all collections
    """
    def getAllCollections(self, dbName = None):
        collections = []
        if isinstance(dbName, str):
            db = self.getDB(dbName)
            collections = db.list_collection_names()            
        else:
            dbList = self.getAllDB()
            for db in dbList:
                collections.extend(self.getDB(db).list_collection_names())
        return collections
    
    
    



    """
    Insert a row in a table
    """
    def insertInto(self, dbName, collectionName, data):
        collection = self.getCollection(dbName,collectionName)
        if isinstance(data, list):
            collection.insert_many(data)
            logging.info("[{}] : Inserted {} rows into {} collection of {}".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"),str(len(data)), collectionName, dbName))
        elif isinstance(data, dict):            
            collection.insert_one(data)
            logging.info("[{}] : Inserted a row into {} collection of {} database with values {}".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"),collectionName, dbName,str(data)))
        elif isinstance(data, pd.DataFrame):
            data = list(data.to_dict(orient='index').values())            
            collection.insert_many(data)
            logging.info("[{}] : Inserted {} rows into {} collection of {}".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"),str(len(data)), collectionName, dbName))
        else:
            logging.info("[{}] : Data type not supported for insertion. Expected list of dict/ dict, Found {}".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"),str(type(data))))
            raise TypeError("Data type not supported for insertion. Expected list of dict/ dict, Found {}".format(str(type(data))))
            
    
    

    """
    Get data of a table
    """
    def getFrom(self, dbName, collectionName, top=10, data_type = 'dataframe', filter_criteria = None):
        try:
            collection = self.getCollection(dbName, collectionName)
            data = collection.find({})
            if data_type == 'dataframe':
                data = pd.DataFrame(data)
            elif data_type == 'models':
                json_data = {}
                for i in data:
                    json_data = i
                data = json_data
            return data
        except:
            logging.info("[{}] : Error in Querying {} collection of {} database".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"),collectionName, dbName))
            raise ValueError("No Data found with given name")
    
