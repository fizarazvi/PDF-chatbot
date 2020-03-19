# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 19:35:04 2020

@author: Srinath Ravikumar
"""

#from Factory import ??
from rake_nltk import Rake
from Processor import QuesDataToElasticSearch, ElasticSearchToEmbeddings, EmbeddingsToQANet

"""
Driver class for processing the query and data, delivering final answer to the UI
"""


class QueryProcessor():
    def __init__(self, query):
        self.__query = query;
        print(query)


"""
Steps:
1. Get data from Database layer.
2. Apply RAKE on query.
3. Feed raked query and raked data to QuesDataToElasticSearch, get result selected_raked_para.
4. Match result selected_raked_para with text paragraphs in data, get selected_text_para .
5. Feed text query and selected_text_para to ElasticSearchToEmbeddings, get vectors query_vec and para_vec.
6. Feed vectors query_vec and para_vec to EmbeddingsToQANet, get test answer.
7. Return text answer :)
"""