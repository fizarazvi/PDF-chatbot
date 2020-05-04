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

    def createChunks(self, text_path):
        text_file_ptr = open(text_path)
        chunks = []
        text = text_file_ptr.read()
        self.generateTitles(chunks, text)
        self.generatePara(chunks, text)
        self.generateKeywords(chunks)

    def generateTitles(self, chunks, text):
        table_of_content = re.findall("(?!\s)[\w\s&\-\,\_\?\&\'\(\)\:\/]+\.\.+\s\d+", text)
        for title in table_of_content:
            temp = Chunks()
            temp.setTitle(title.split(".")[0])
            chunks.append(temp)

    def generatePara(self, chunks, text):
        chunk_len = len(chunks)

        # split the text file on the first occurance of the last title
        content = text.split(chunks[chunk_len - 1]._Chunks__title, 1)

        for i in range(0, chunk_len):
            temp = chunks[i]
            if i != chunk_len - 1:
                para = re.findall(
                    re.escape(chunks[i]._Chunks__title) + "[\w\s\W]+" + re.escape(chunks[i + 1]._Chunks__title),
                    content[1], flags=re.IGNORECASE)
            else:
                para = re.findall(re.escape(chunks[i]._Chunks__title) + "[\w\s\W]+", content[1], flags=re.IGNORECASE)
            temp.setPara(" ".join(para))


    def generateKeywords(self, chunks):
        r = Rake()
        for chunk in chunks:
            text = chunk._Chunks__para
            r.extract_keywords_from_text(text)
            chunk.setKeywords(r.get_ranked_phrases_with_scores())
        for chunk in chunks:
            print(chunk._Chunks__title)
            print(chunk._Chunks__para)
            print(chunk._Chunks__keywords)
            print("\n**\n")


"""
Each chunk has a title, a paragraph under that title and keywords in that particular paragraphs
and a list of such chunks is created by the above class object
"""
