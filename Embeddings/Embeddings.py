# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 11:05:54 2020

@author: Ratan Singh
"""

from abc import ABC

"""
Defining the Abstratc Class
"""

class Embeddings(ABC):
      
    """
    Will load the embedding model and oredict the embeddings from text
    """
    def load(self):
        pass


    def predict(self, data):
        pass
