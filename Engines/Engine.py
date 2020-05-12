# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 13:01:00 2020

@author: Ratan Singh
"""

from abc import ABC

class Engine(ABC):
        
    def train(self, trainData):
        pass
    
    
    def predict(self, testData):
        pass  