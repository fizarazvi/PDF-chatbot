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
from Factory.DatabaseFactory import DatabaseFactory
from ConfigParser.ConfigParser import ConfigurationParser
from Processor.PDFProcessor import PDFProcessor
from Processor.QuesDataToElasticSearch import QuesDataToElasticSearch
from Processor.WMD import WMD
from ElasticServer import ElasticServer

"""
Driver class for processing the query and data, delivering final answer to the UI
"""


class QueryProcessor(Engine):

    # Never instatiate a class with some object that will chnage again and again.
    # Hence removing parameter query from here.

    def __init__(self):
        LOG_FILE = "logs/queryProcessor.log"
        self.__logger = logging.getLogger("queryProcessor")
        file_handler = logging.FileHandler(LOG_FILE)
        self.__logger.addHandler(file_handler)

        self.__config = ConfigurationParser()
        self.__database = DatabaseFactory().getDatabase(self.__config.getEngineConfig("SmartPDFAssistant")['database'])

        # Will implement in later stages

    def searchInElasticServer(self, query):
        es = ElasticServer()
        selected_titles = es.get_shard("esindex", query)
        print("selected_titles : ", selected_titles)
        return selected_titles

    def train(self, pdfname):
        print("\n pdfname : "+pdfname)
        processed = PDFProcessor(pdfname)
        processed.processPdf(pdfname)

    # Will take the query and return the output
    def predict(self, query):

        # Logging the query
        self.__logger.info("[{}] : Received Query : {}".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), query))

        """
        Fill in your logic to procss the query here.
        Curently this will return the same question as response from here.
        """

        # Applying RAKE on query.
        r = Rake()
        query_keywords = r.extract_keywords_from_text(query)
        query_ranked_phrase = r.get_ranked_phrases()
        query = ''.join(query_ranked_phrase)

        print("query_ranked_phrase : ", query_ranked_phrase)
        print("query : ", query)

        # Creating objects
        wmd = WMD()
        qp = QueryProcessor()

        selected_titles = qp.searchInElasticServer(query)

        if not selected_titles:
            return "No results found!"

        #for i in selected_titles:
            #response.append(wmd.predict(query_ranked_phrase, selected_titles[i]))

        db_data = self.__database.getFrom("PDFAssistant", "ProcessedPDF", '')
        print("Titles\n", db_data['Title'])
        print("Text\n", db_data['Text'])

        # Temporary code to bypass WMD Glove component
        i = 0
        length = len(db_data['Title'])
        while i < length:
            if selected_titles[7] == db_data['Title'][i]:
                break
            i += 1

        response = db_data['Text'][i]
        print("response : ", response)


        # Logging the response
        self.__logger.info("[{}] : Answer Sent : {}".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), response))
        self.__logger.info("--" * 30)

        # Insertion into DB
        self.__database.insertInto("PDFAssistant", "QueryHistory",
                                   {'Date': datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'Query': query,
                                    'Answer': response})

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
