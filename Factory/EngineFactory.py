# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 22:26:22 2020
@author: Ratan Singh
"""
from datetime import datetime
import logging

from Utilities.Singleton  import Singleton

class EngineFactory(metaclass = Singleton):
    
    def __init__(self):
        pass
    
    def getEngine(self,engineType):
        supportedEngines = ['SupportTicketEngine','Dummy']
        engineType = [x for x in supportedEngines if x.lower() == engineType.lower()][0]
        try:
            print("from Engine.{} import {}".format(engineType, engineType))
            exec("from Engine.{} import {}".format(engineType,engineType))
            print("Ram")
            engine = eval(engineType+"()")
            logging.info("[{}] : Engine object of type {} created.".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"),engineType))
            return engine
        except:
            logging.info("[{}] : Engine type {} not supported".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), engineType))
            raise TypeError("Engine Type {} not supported.".format(engineType))
        
            
        
        
        