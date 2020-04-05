# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 15:25:29 2020

@author: Ratan Singh
"""

from configparser import ConfigParser
from Utilities.Singleton import Singleton

class ConfigurationParser(metaclass = Singleton):
    
    def __init__(self):
        self.__config = ConfigParser()
        self.__config.read("config.ini")
    
    """
    Returns the Configuration for the Server
    """
    def getServerConfig(self):
        try:
            return dict(self.__config['Server'])
        except:
            raise ValueError('No Configurations found for Server')
            
    
    """
    Returns the configuration for Engine
    """
    def getEngineConfig(self, engineName):
       try:
           database = self.__config[engineName]['database'] if 'database' in list(self.__config[engineName]) else 'Database'
           serverDefault = self.getServerConfig()
           databaseDefault = self.getDatabaseConfig(database)
           return dict(self.__config[engineName])
       except:
           raise ValueError('No Configurations found for Engine {}'.format(engineName))
    
    
    
    """
    Returns the configuration of Database
    """
    
    def getDatabaseConfig(self, databaseName = 'Database'):
        try:
            return dict(self.__config[databaseName])
        except:
            raise ValueError("No Configurations found for Database {}".format(databaseName))
        