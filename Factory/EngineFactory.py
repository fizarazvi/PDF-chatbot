# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 22:26:22 2020

@author: Ratan Singh
"""
from datetime import datetime
import logging

from Engine.SupportTicketEngine import SupportTicketEngine

class EngineFactory():
    
    def __init__(self):
        pass
    
    def getEngine(engineType):
        try:
            database = eval(engineType.capitalize()+"()")
            logging.info("[{}] : Engine object of type {} created.".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"),engineType))
            return database
        except:
            logging.info("[{}] : Engine type {} not supported".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), engineType))
            raise TypeError("Engine Type {} not supported.".format(engineType))
        
            
        
        
        