from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

from Processor.Processor import Processor
from Utilities.Singleton import Singleton

"""
PDFToText
This class provides an facility to read PDF page by page and writes them into a text file
    - extractTextByPage : Creates a comprehensive text of PDF
    - extractText :  writes the text to .txt handle
"""


class PDFToText(Processor):

    def __init__(self):
        __metaclass__ = Singleton
        self.__text = ""


    def extractTextByPage(self, pdf_path):
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

    def extractText(self, pdf_path):
        text_path = '../uploads/' + pdf_path.rsplit('/', 1)[-1][:-4] + '-text.txt'
        out_ptr = open(text_path, "w")
        for page in self.extractTextByPage(pdf_path):
            out_ptr.write(page)
        out_ptr.close()
        return text_path
