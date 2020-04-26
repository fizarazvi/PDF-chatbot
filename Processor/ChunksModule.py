"""
This class provides a format to define a chunk having title, paragraph and keywords
    setTitle: assigns title to the chunk object
    setPara: assigns paragraph to the chunk object
    setKeywords: assigns keywords from the paragraph to the chunk object
"""
class Chunks():
    def __init__(self):
        self.__title = ""
        self.__para = ""
        self.__keywords = []

    def setTitle(self, title):
        self.__title = title

    def setPara(self, para):
        self.__para = para

    def setKeywords(self, keywords):
        self.__keywords = keywords
