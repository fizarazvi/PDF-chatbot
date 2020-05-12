# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 22:25:22 2020

@author: Ratan Singh
"""

import logging
from datetime import datetime

from Factory.DatabaseFactory import DatabaseFactory
from Factory.EngineFactory import EngineFactory
from Utilities.Singleton import Singleton

class Factory(metaclass = Singleton):
    
    """
    Instance Class : Database , Engine
    """

    def getInstance(self, instanceClass, instanceType):

        if not instanceClass.lower() in ["database", "engine"]:
            raise ValueError("Factory of Type {} is not supported.".format(instanceClass))
        try:
            return eval(instanceClass.capitalize()+"Factory().get"+instanceClass.capitalize()+"("+instanceType()+")")
        except:
            logging.info("[{}] : Error in creating instance of {} of type {}".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), instanceClass, instanceType))
            raise ValueError("Error in creating instance of {} of type {}.".format(instanceClass, instanceType))
