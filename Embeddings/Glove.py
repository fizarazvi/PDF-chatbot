# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 16:08:05 2020

@author: Ratan Singh
"""

import numpy as np
from word_mover_distance import model

from Embeddings.Embeddings import Embeddings
from Utilities.Singleton import Singleton


class Glove(Embeddings):
    
    glove = {}
    
    def __init__(self):
        __metaclass__ = Singleton
        self.__modelPath = "F://OFFICIAL//SMART PDF ASSISTANT//Smart-pdf-assistant//ThirdPartyData//glove.6B//glove.6B.50d.txt"
        
        
    def load(self):
        try:
            # Change Glove vector path to your specific local location
            wmdmodel = model.WordEmbedding(model_fn="F://OFFICIAL//SMART PDF "
                                                    "ASSISTANT//Smart-pdf-assistant//ThirdPartyData//glove.6B//glove.6B"
                                                    ".50d.txt")
        except:
            raise Exception("Glove vectors not found, check local path")

        return wmdmodel
    
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