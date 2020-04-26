import re
from rake_nltk import Rake
from ChunksModule import Chunks

"""
This class ExtractChunks provide the facilty to break the text file into list of chunks(title, paragraph, keywords)
    createChunks: to generate a list of chunk from text file
    generateTitles: get titles(headers) from the text file
    generateParagraph: get paragraphs between two titles of text file
    generateKeywords: get keywords from each paragraph 
"""

class ExtractChunks():
    def __init__(self, text_path):
        self.__chunks = []
        self.__text_path = text_path
        self.__text = ""

    def createChunks(self):
        text_file_ptr = open(self.__text_path)
        self.__text = text_file_ptr.read()
        self.generateTitles()
        self.generatePara()
        self.generateKeywords()


    def generateTitles(self):
        table_of_content =  re.findall("[\w\s&\(\)]+\s\.+\s*\d+", self.__text)
        for title in table_of_content:
            temp = Chunks()
            temp.setTitle(title.split(".")[0].split(" ",1)[1])
            self.__chunks.append(temp)

    def generatePara(self):
        chunk_len = len(self.__chunks)
        content = self.__text.split(self.__chunks[chunk_len-1]._Chunks__title)
        for i in range(0,chunk_len-2):
            temp = self.__chunks[i]
            para = re.findall(self.__chunks[i]._Chunks__title+"[\w\s\W]+"+self.__chunks[i+1]._Chunks__title, content[1])
            temp.setPara(" ".join(para))

    def generateKeywords(self):
        r = Rake()
        for chunk in self.__chunks:
            text = chunk._Chunks__para
            r.extract_keywords_from_text(text)
            chunk.setKeywords(r.get_ranked_phrases_with_scores())
        for chunk in self.__chunks:
            print(chunk._Chunks__title)

"""
Each chunk has a title, a paragraph under that title and keywords in that particular paragraphs
and a list of such chunks is created by the above class object
"""