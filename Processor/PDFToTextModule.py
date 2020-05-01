from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

"""
PDFToText
This class provides an facility to read PDF page by page and writes them into a text file
    - extractTextByPage : Creates a comprehensive text of PDF
    - extractText :  writes the text to .txt handle
"""
class PDFToText():
    def __init__(self, pdf_path):
        self.__pdf_path = pdf_path
        self.__text_path = '../SampleText/' + pdf_path.rsplit('/',1)[-1][:-4] + '-text.txt'
        self.__out_ptr = open(self.__text_path, "w")

    def extractTextByPage(self):
        with open(self.__pdf_path, 'rb') as fh:
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

    def extractText(self):
        for page in self.extractTextByPage():
            self.__out_ptr.write(page)


