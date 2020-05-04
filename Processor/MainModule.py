import argparse

from ExtractChunksModule import ExtractChunks
from PDFToTextModule import PDFToText

"""
    PDFParser
    This class provides a facility of parsing pdf to chunks
"""


class PDFParser():
    def __init__(self):
        self.__pdf_path = ''
        self.__text_path = ''

    def parsePdf(self):
        parser = argparse.ArgumentParser(description="Enter document filename")
        parser.add_argument('doc', help='document filename')
        args = parser.parse_args()
        self.__pdf_path = '../uploads/' + args.doc  # input document filename
        pdf_to_text = PDFToText()
        self.__text_path = pdf_to_text.extractText(self.__pdf_path)
        extract_chunk = ExtractChunks()
        extract_chunk.createChunks(self.__text_path)


"""
This class ultimately provide a list of chunks from the pdf file by parsing it to text file using PDFToText and then ExtractChunks
"""

if __name__ == '__main__':
    pdfParser = PDFParser()
    pdfParser.parsePdf()
