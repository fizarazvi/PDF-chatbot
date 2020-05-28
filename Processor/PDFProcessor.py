"""
 Created by Fiza 
 on 14 2020 03:40 PM
"""
import argparse
from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

import re
from rake_nltk import Rake
from datetime import datetime
from Factory.DatabaseFactory import DatabaseFactory
from ConfigParser.ConfigParser import ConfigurationParser
from ElasticServer import ElasticServer

# commented following lines, issues while importing them
# from Processor.Processor import Processor
# from Utilities.Singleton import Singleton



"""
    PDFParser
    This class provides a facility of parsing pdf to chunks
"""


class PDFProcessor:
    def __init__(self, pdfname):
        # args = parser.parse_args()
        self.__pdfname = pdfname

    def processPdf(self, pdfname):
        # parser = argparse.ArgumentParser(description="Enter document filename")
        # parser.add_argument('doc', help='document filename')
        # args = parser.parse_args()
        pdf_path = 'uploads/' + pdfname  # input document filename
        text_path = self.__extractText(pdf_path)
        processed_pdf = self.__createChunks(text_path)
        self.__addToDatabase(processed_pdf)
        self.__addToElasticServer(processed_pdf)

    def __extractText(self, pdf_path):
        text_path = 'uploads/' + pdf_path.rsplit('/', 1)[-1][:-4] + '-text.txt'
        out_ptr = open(text_path, "w")
        for page in self.__extractTextByPage(pdf_path):
            out_ptr.write(page)
        out_ptr.close()
        return text_path

    def __extractTextByPage(self, pdf_path):
        with open(pdf_path, 'rb') as fh:
            for page in PDFPage.get_pages(fh,
                                          caching=True,
                                          check_extractable=True):
                resource_manager = PDFResourceManager()
                fake_file_handle = StringIO()
                converter = TextConverter(resource_manager, fake_file_handle)
                page_interpreter = PDFPageInterpreter(resource_manager, converter)
                page_interpreter.process_page(page)

                text = fake_file_handle.getvalue().encode('ascii', 'ignore').decode()

                yield text
                # close open handles
                converter.close()
                fake_file_handle.close()

    def __createChunks(self, text_path):
        text_file_ptr = open(text_path)
        chunks = []
        text = text_file_ptr.read()
        self.__generateTitles(chunks, text)
        self.__generatePara(chunks, text)
        self.__generateKeywords(chunks)
        return chunks

    def __generateTitles(self, chunks, text):
        table_of_content = re.findall("(?!\s)[\w\s&\-\,\_\?\&\'\(\)\:\/]+\.\.+\s\d+", text)
        for title in table_of_content:
            temp = [title.split(".")[0]]
            chunks.append(temp)

    def __generatePara(self, chunks, text):
        chunk_len = len(chunks)

        content = text.split(chunks[chunk_len - 1][0], 1)

        for i in range(0, chunk_len):
            temp = chunks[i]
            if i != chunk_len - 1:
                para = re.search(
                    re.escape(chunks[i][0]) + "[\w\s\W]+" + re.escape(chunks[i + 1][0]),
                    content[1], flags=re.IGNORECASE)
                if para:
                    para = "{}".format(para.group(0))
                    paragraph = para.replace(chunks[i][0], '', 1)
                    paragraph += para.replace(chunks[i + 1][0], '')
            else:
                para = re.search(re.escape(chunks[i][0]) + "[\w\s\W]+", content[1], flags=re.IGNORECASE)
                if para:
                    para = "{}".format(para.group(0))
                    paragraph = para.replace(chunks[i][0], '')
            temp.append("".join(paragraph))

    def __generateKeywords(self, chunks):
        r = Rake()
        for chunk in chunks:
            text = chunk[1]
            r.extract_keywords_from_text(text)
            chunk.append(r.get_ranked_phrases_with_scores())
        # for chunk in chunks:
        #     print(chunk[0])
        #     print(chunk[1])
        #     print(chunk[2])
        #     print("\n**\n")

    def __addToDatabase(self, chunks):
        self.__config = ConfigurationParser()
        self.__database = DatabaseFactory().getDatabase(self.__config.getEngineConfig("SmartPDFAssistant")['database'])

        for chunk in chunks:
            self.__database.insertInto("PDFAssistant", "ProcessedPDF",{'Date': datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'Title': chunk[0],'Text': chunk[1], 'Keywords': chunk[2]})

    def __addToElasticServer(self, chunks):
        es = ElasticServer()
        pdfName = str(self.__pdfname).lower()
        print("es.index : ", es.createIndex("esindex"))
        es.store_records("esindex", chunks)

"""
This class ultimately provide a list of chunks from the pdf file by parsing it to text file using PDFToText and then ExtractChunks
"""

if __name__ == '__main__':
    pdfParser = PDFProcessor()
    pdfParser.processPdf()
