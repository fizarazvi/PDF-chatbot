# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 19:35:04 2020

@author: Srinath Ravikumar
"""

# Decomission this - We dont need an explicit class to convert data to RAKE. Also ElasticSearch Feeder was supposed to be done by Shubham

from Database.Mongo import Mongo

class QuesDataToElasticSearch():

    def __init__(self):
        pass

    def QuesDataToElasticSearch(self, raked_data, query_ranked_phrase_with_score):
        selected_rake_para = 0

        return selected_rake_para

    def matchRakedParaToTextPara(self, selected_raked_para):
        selected_text_para = db.getFrom("data", "processed_data", """ filter: condition for matching """)

        return selected_text_para

db = Mongo()