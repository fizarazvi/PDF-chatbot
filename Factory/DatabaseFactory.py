# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 22:26:22 2020

@author: Ratan Singh
"""
from datetime import datetime
import logging

from Database.Mongo import Mongo
from Utilities.Singleton import Singleton

class DatabaseFactory(metaclass = Singleton):
    
    def __init__(self):
        pass
    
    def getDatabase(self,databaseType):
        try:
            database = eval(databaseType.capitalize()+"()")
            logging.info("[{}] : Database object of type {} created.".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"),databaseType))
            return database
        except:
            logging.info("[{}] : Database type {} not supported".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), databaseType))
            raise TypeError("Database Type {} not supported.".format(databaseType))
        
            
        
        
        