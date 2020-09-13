# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 19:35:04 2020

@author: Srinath Ravikumar
"""

import logging
from datetime import datetime
from rake_nltk import Rake
from operator import itemgetter

from Engines.Engine import Engine
from Factory.DatabaseFactory import DatabaseFactory
from ConfigParser.ConfigParser import ConfigurationParser
from Processor.PDFProcessor import PDFProcessor
from Processor.WMD import WMD
from ElasticServer import ElasticServer

"""
Driver class for processing the query and data, delivering final answer to the UI
"""


class QueryProcessor(Engine):

    def __init__(self):
        LOG_FILE = "logs/queryProcessor.log"
        self.__logger = logging.getLogger("queryProcessor")
        file_handler = logging.FileHandler(LOG_FILE)
        self.__logger.addHandler(file_handler)

        self.__config = ConfigurationParser()
        self.__database = DatabaseFactory().getDatabase(self.__config.getEngineConfig("SmartPDFAssistant")['database'])


    def searchInElasticServer(self, query):
        es = ElasticServer()
        selected_titles = es.get_shard("esindex", query)
        return selected_titles

    def train(self, pdfname):
        print("\n pdfname : "+pdfname)
        processed = PDFProcessor(pdfname)
        processed.processPdf(pdfname)

    def merge(self, list1, list2):
        merged_list = tuple(zip(list1, list2))
        return merged_list

    # Will take the query and return the output
    def predict(self, query, wmdmodel):

        # Logging the query
        self.__logger.info("[{}] : Received Query : {}".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), query))

        # Applying RAKE on query.
        r = Rake()
        query_keywords = r.extract_keywords_from_text(query)
        query_ranked_phrase = r.get_ranked_phrases()
        query = ''.join(query_ranked_phrase)

        # Creating objects
        wmd = WMD()
        qp = QueryProcessor()

        # Searching for titles matched with query in elastic server
        selected_titles = qp.searchInElasticServer(query)
        selected_titles_len = len(selected_titles)

        if not selected_titles:
            return "No results found!"

        # Using WMD to get vector distance between query and each of the selected titles
        wmdresponse = wmd.getWMDResponse(wmdmodel, query, selected_titles, selected_titles_len)

        response = self.merge(selected_titles, wmdresponse)

        # Sorting response according to vector distance (ascending)
        response = sorted(response, key=itemgetter(1))

        # Retrieving preprocessed data from DB
        db_data = self.__database.getFrom("PDFAssistant", "ProcessedPDF", '')

        # Selecting title having minimum vector distance with input query
        for i in range(len(db_data['Title'])):
            if response[0][0] == db_data['Title'][i]:
                break;

        finalresponse = db_data['Text'][i]

        if not finalresponse:
            return "No results found! Please refine your search"

        # Logging the response
        self.__logger.info("[{}] : Answer Sent : {}".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), finalresponse))
        self.__logger.info("--" * 30)

        # Insertion into DB
        self.__database.insertInto("PDFAssistant", "QueryHistory",
                                   {'Date': datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'Query': query,
                                    'Answer': finalresponse})

        return finalresponse


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
