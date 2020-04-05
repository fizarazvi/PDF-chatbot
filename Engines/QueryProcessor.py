# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 19:35:04 2020

@author: Srinath Ravikumar
"""

import logging
from datetime import datetime

#from Factory import ??
from Engines.Engine import Engine
from rake_nltk import Rake
from Processor import QuesDataToElasticSearch, ElasticSearchToEmbeddings, EmbeddingsToQANet

"""
Driver class for processing the query and data, delivering final answer to the UI
"""


class QueryProcessor(Engine):
    
    # Never instatiate a class with some object that will chnage again and again.
    # Hence removing parameter query from here.
    def __init__(self):
        self.__query = None
        logging.basicConfig(filename="logs/queryProcessor.log", filemode='w', level=logging.DEBUG)    
    
    
    
    # Will implement in later stages
    def train(self, trainData):
        pass
        

    # Will take the query and return the output
    def predict(self, query):
        
        #Logging the query
        logging.info("[{}] : Received Query : {}".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), query))


        
        """
        Fill in your logic to procss the query here.
        Curently this will return the same question as response from here.
        """
        response = query
        

        # Example of storing something in database
        
        
        #Logging the response
        logging.info("[{}] : Answer Sent : {}".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), response))
        logging.info("--"*30)

        return response
    


"""
Steps:
1. Get data from Database layer. (Incorrect - Query will come for HTTP request)
2. Apply RAKE on query.
3. Feed raked query and raked data to QuesDataToElasticSearch, get result selected_raked_para.
4. Match result selected_raked_para with text paragraphs in data, get selected_text_para .
5. Feed text query and selected_text_para to ElasticSearchToEmbeddings, get vectors query_vec and para_vec.
6. Feed vectors query_vec and para_vec to EmbeddingsToQANet, get test answer.
7. Return text answer :)
"""