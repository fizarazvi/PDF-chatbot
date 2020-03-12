# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 22:15:00 2020

@author: Ratan Singh
"""

from abc import ABC

class Database(ABC):
    
    def __connect(self):
        pass
    
    def getDB(self):
        pass
    
    def getAllDB(self):
        pass
    
    def getCollection(self):
        pass
    
    def getAllCollections(self):
        pass
    
    def insertInto(self):
        pass
    
    def getFrom(self):
        pass
