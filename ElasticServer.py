from elasticsearch import Elasticsearch
import logging
from datetime import datetime
import pandas as pd
import json

from Utilities.Singleton import Singleton
from ConfigParser.ConfigParser import ConfigurationParser


class ElasticServer:
    def __init__(self):
        # This makes class singleton
        __metaclass__ = Singleton

        # Instating Logger
        LOG_FILE = "logs/ElasticServer.log"
        self.__logger = logging.getLogger("Elastic Server")
        file_handler = logging.FileHandler(LOG_FILE)
        self.__logger.addHandler(file_handler)
        self._connect()

    def _connect(self):
        # connecting to the elastic server
        try:
            # get the elastic server details from  the config file
            self.__config = ConfigurationParser()
            self.__port = int(self.__config.getElasticServerConfig()['port'])
            self.__host = self.__config.getElasticServerConfig()['host']

            # Connect to the elastic server
            self.__es = Elasticsearch([{'host': self.__host, 'port': self.__port}])
            self.__logger.info("[{}] : Successfully connected to Elastic server at {}".format(
                datetime.now().strftime("%d/%m/%Y %H:%M:%S"), self.__host + ":" + str(self.__port)))
            self.__logger.info("==" * 30)
            print(self.__es)
        except:
            logging.error(
                "[{}] : Could not connect to Elastic server.".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
            raise ConnectionError("Could not connect to Elastic server.")

    def createIndex(self, index_name):
        created = False
        settings = {  # Not used
            "settings": {
                "number_of_shards": 1,  # change according to number of chunks
                "number_of_replicas": 0
            },
            "mappings": {
                "properties": {
                    "id": {
                        "type": "integer"
                    },
                    "Title": {
                        "type": "text"
                    },
                    "Keywords": {
                        "type": "text"
                    },
                    "Paragraph": {
                        "type": "text"
                    }
                }
            }
        }
        try:
            if not self.__es.indices.exists(index_name):
                # Ignore 400 means to ignore "Index Already Exist" error.
                res = self.__es.indices.create(index=index_name, ignore=400, body=settings)
                print("Response:" + str(res))
                print('Created Index')
                created = True
        except Exception as ex:
            print(str(ex))
        finally:
            return created
        
    # Not used
    def add_document(self, index_name, doc_type, doc, doc_id=None):
        resp = self.__es.index(index=index_name, doc_type=doc_type, body=doc, id=doc_id)
        print(resp)
        print("Document created")

    def store_records(self, index_name):
        # later records can be read from a file
        rec1 = {
            "id": 1,
            "Title": "Overview",
            "Keywords": "Hello, this, is, a, test.",
            "Paragraph": "Hello this is a test and a test this is."
        }
        rec2 = {
            "id": 2,
            "Title": "Intro",
            "Keywords": "Hello, this, is, a, test.",
            "Paragraph": "Hello this is a test and a test this is."
        }
        rec3 = {
            "id": 3,
            "Title": "Topic 1",
            "Keywords": "Hello, this, is, a, test.",
            "Paragraph": "Hello this is a test and a test this is."
        }
        try:
            outcome = self.__es.index(index=index_name, body=rec1)
        except Exception as ex:
            print('Error in indexing data')
            print(str(ex))
        try:
            outcome = self.__es.index(index=index_name, body=rec2)
        except Exception as ex:
            print('Error in indexing data')
            print(str(ex))
        try:
            outcome = self.__es.index(index=index_name, body=rec3)
        except Exception as ex:
            print('Error in indexing data')
            print(str(ex))

    def get_shard(self, index_name ):
        # es = connect_elasticsearch()
        if self.__es is not None:
            search_object = json.dumps({
                "query": {
                    "match": {
                        "Title": "Overview"
                    }
                }
            })
            resp = self.__es.search(index=index_name, body=search_object)
        print("Record:")
        print(resp)
        # Returning a response but it does not contain the details of the record.



"""res = es.index(index='megacorp',doc_type='employee',id=1,body=e1)
res = es.index(index='megacorp',doc_type='employee',id=2,body=e2)
res = es.index(index='megacorp',doc_type='employee',id=3,body=e3)
res=es.get(index='megacorp',doc_type='employee',id=3)
print (res['_source'])"""
