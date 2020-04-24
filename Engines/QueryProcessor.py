from rake_nltk import Rake

# from Processor import QuesDataToElasticSearch, ElasticSearchToEmbeddings, EmbeddingsToQANet

"""
Driver class for processing the query and data, delivering final answer to the UI
"""


class QueryProcessor:
    def __init__(self, query):
        self.__query = query
        print(query)

    def return_answer(self):
        return self.__query.upper()
