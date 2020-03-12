# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 22:25:22 2020

@author: Ratan Singh
"""

import logging
from datetime import datetime
from DatabaseFactory import DatabaseFactory

class Factory():
    
    def getInstance(self, instanceClass, instanceType):
        try:
            return eval(instanceClass.capitalize()+"("+instanceType.capitalize()+")")
        except:
            logging.info("[{}] : Error in creating instance of {} of type {}".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), instanceClass, instanceType))
            raise ValueError("Error in creating instance of {} of type {}.".format(instanceClass, instanceType))