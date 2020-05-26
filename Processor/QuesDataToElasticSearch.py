# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 19:35:04 2020

@author: Srinath Ravikumar
"""

from Database.Mongo import Mongo
from ElasticServer import ElasticServer

class QuesDataToElasticSearch():

    def __init__(self):
        pass

    def QuesDataToElasticSearch(self, query):
        es = ElasticServer()
        selected_titles = es.get_shard("esindex", query)
        print("selected_titles : ", selected_titles)
        return selected_titles


