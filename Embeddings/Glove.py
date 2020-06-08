# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 16:08:05 2020

@author: Ratan Singh
"""

import numpy as np

from Embeddings.Embeddings import Embeddings
from Utilities.Singleton import Singleton


class Glove(Embeddings):
    
    glove = {}
    
    def __init__(self):
        __metaclass__ = Singleton
        self.__modelPath = "ThirdPartyData//glove.6B.50d.txt"
        
        
    def load(self):
        if self.glove == {}:
            try:
                with open(self.__modelPath, 'r', encoding = 'utf8') as f:
                    for line in f:
                        values = line.split()
                        word = values[0]
                        vector = np.array([float(value) for value in values[1:]])
                        self.glove[word] = vector
            except:
                raise Exception("Exception occured in reading the glove data.")
        else:
            pass
    
    def __predict(self, data):
        try:
            return self.glove[data]
        except:
            return np.zeros(50)
        
        
    
    def predict(self, data):
        
        if isinstance(data, str):
            return self.__predict(data.lower())
        
        elif isinstance(data, list):
            embedding = []
            for token in data:
                embedding.append(self.__predict(token.lower()))
            return embedding
        
        else:
            raise Exception("Data type not supported.")