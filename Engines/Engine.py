# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 11:05:54 2020

@author: Ratan Singh
"""

from abc import ABC

"""
Defining the Abstract Class
"""

class Engine(ABC):
    
    
    
    """
    Will update the model objects with new data and
    store them back in the database
    """
    def train(self, trainData):
        pass
    
    
    
    
    """
    Will load the model from database and predict the output
    """
    def predict(self, testData):
        pass