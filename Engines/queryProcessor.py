# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 19:35:04 2020

@author: Srinath Ravikumar
"""


import logging
from datetime import datetime
from rake_nltk import Rake
from nltk.corpus import stopwords

from Engines.Engine import Engine
from Database import Mongo
from Processor import QuesDataToElasticSearch, ElasticSearchToEmbeddings, EmbeddingsToQANet

"""
Driver class for processing the query and data, delivering final answer to the UI
"""


class QueryProcessor(Engine):

    # Never instatiate a class with some object that will chnage again and again.
    # Hence removing parameter query from here.

    

    def __init__(self):

        LOG_FILE = "logs/queryProcessor.log"
        self.__logger = logging.getLogger("queryProcessorr")
        file_handler = logging.FileHandler(LOG_FILE)
        self.__logger.addHandler(file_handler)
        
        self.__query = ""
        
        # Will implement in later stages

    def train(self, trainData):
        pass

    # Will take the query and return the output
    def predict(self, query):
        #query = "This is a sample query"

        # Logging the query
        self.__logger.info("[{}] : Received Query : {}".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), query))

        """
        Fill in your logic to procss the query here.
        Curently this will return the same question as response from here.
        """
        print("query : ", query)

        # Applying RAKE on query.
        r = Rake()
        query_keywords = r.extract_keywords_from_text(query)
        query_ranked_phrase = r.get_ranked_phrases()
        query_ranked_phrase_with_score = r.get_ranked_phrases_with_scores()

        print("query_ranked_phrase_with_score : ", query_ranked_phrase_with_score)

        # Creating objects
        process = QueryProcessor()
        db = Mongo.Mongo()
        elasticSearch = QuesDataToElasticSearch.QuesDataToElasticSearch()
        embeddings = ElasticSearchToEmbeddings.ElasticSearchToEmbeddings()
        qaNet = EmbeddingsToQANet.EmbeddingsToQANet()

        # get data from database layer
        raked_data = db.getFrom("data","processed_data")  # yet to decide

        # Feed raked query and raked data to QuesDataToElasticSearch, get result selected_raked_para
        selected_raked_para = elasticSearch.QuesDataToElasticSearch(raked_data, query_ranked_phrase_with_score)

        # Match result selected_raked_para with text paragraphs in data, get selected_text_para .
        selected_text_para = elasticSearch.matchRakedParaToTextPara(selected_raked_para)

        # Feed text query and selected_text_para to ElasticSearchToEmbeddings, get vectors query_vec and para_vec
        query_vec = embeddings.ElasticSearchToEmbeddings(query, "query")
        para_vec = embeddings.ElasticSearchToEmbeddings(selected_text_para, "data")

        # Feed vectors query_vec and para_vec to EmbeddingsToQANet, get test answer.
        response = qaNet.EmbeddingsToQANet(query_vec, para_vec)


        # Example of storing something in database

        # Logging the response
        self.__logger.info("[{}] : Answer Sent : {}".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), response))
        self.__logger.info("--" * 30)

        return response

"""
Steps:
1. Get data from Database layer. Query will come for HTTP request.
2. Apply RAKE on query.
3. Feed raked query and raked data to QuesDataToElasticSearch, get result selected_raked_para.
4. Match result selected_raked_para with text paragraphs in data, get selected_text_para .
5. Feed text query and selected_text_para to ElasticSearchToEmbeddings, get vectors query_vec and para_vec.
6. Feed vectors query_vec and para_vec to EmbeddingsToQANet, get test answer.
7. Return text answer :)
"""