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
            #print(self.__es)
        except:
            print("Could not Connect to Elastic Server")
            raise ConnectionError("Could not connect to Elastic server.")

    def createIndex(self, index_name):
        created = False
        settings = {  
            "settings": {
                "number_of_shards": 1,  # change according to number of chunks
                "number_of_replicas": 0
            },
            "mappings": {
                "Chunks": {
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
        }
        try:
            if not self.__es.indices.exists(index_name):
                # Ignore 400 means to ignore "Index Already Exist" error.
                # res = self.__es.indices.create(index=index_name, ignore=400, body=settings)
                res = self.__es.indices.create(index=index_name, ignore=400)
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

    def store_records(self, index_name, chunks):
        # later records can be read from a file
        for chunk in chunks:
            rec1 = {
                "Title": chunk[0],
                "Text": chunk[1],
                "Keywords": str(chunk[2])
            }
            try:
                outcome = self.__es.index(index=index_name, doc_type='Chunks', body=rec1)
            except Exception as ex:
                print('Error in indexing data')
                print(str(ex))
        # self.__es.transport.close()

    def get_shard(self, index_name, query):
        # self._connect()
        # self.__es.createIndex(index_name)
        # resp = self.__es.get(index=index_name, doc_type="Chunks", id=1)
        if self.__es is not None:
            search_object = json.dumps({
                "query": {
                    "match": {  # or use match/ aggregations?
                        "Text":query
                    }
                }
            })
            search_object = json.dumps({
                "query": {
                    "more_like_this" : {
                        "fields": ["Title", "Text"],
                        "like": query,
                        "min_term_freq": 1,
                        "max_query_terms": 12
                    }
                }
            })
            resp = self.__es.search(index=index_name, doc_type="Chunks", body=search_object)
            #print("Record:")
            #print(resp["hits"]["hits"][:3])

        selected_titles = []
        for hit in resp["hits"]["hits"]:
            selected_titles.append(hit['_source']['Title'])

        return selected_titles
