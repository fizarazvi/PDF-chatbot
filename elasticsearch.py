from elasticsearch import Elasticsearch

from SmartPDF.ConfigParser.ConfigParser import getDatabaseConfig

DB_HOST = getDatabaseConfig('MongoDB')

elasticsearch_client = Elasticsearch(hosts = [{"host" : DB_HOST}])
