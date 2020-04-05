# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 11:05:54 2020

@author: Ratan Singh
"""

from abc import ABC

"""
Defining the Abstratc Class
"""

class Processor(ABC):
      
    """
    Will load the model from database and predict the output
    """
    def predict(self, testData):
        pass