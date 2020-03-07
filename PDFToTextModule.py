from io import StringIO
import re


from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

from rake_nltk import Rake

# @Fiza - Separate each class into other files for better readability. Before you commit, your code put some extra lines as brief
# documentation of class the way I have put here. Please use camelCase for naming.  


"""
PDFToText
This class provides an facility to read PDF page by page and writes them into a text file
    - extract_text_by_page : Creates a comprehensive text of PDF
    - extract_text :  writes the text to .txt handle
"""
class PDFToText():
    def __init__(self, pdf_path):
        self.pdf_path = 'SamplePdf/' + pdf_path
        self.text_path = 'SampleText/' + pdf_path[:-4] + '-text.txt'
        self.out_ptr = open(self.text_path, "w")

    def extract_text_by_page(self):
        with open(self.pdf_path, 'rb') as fh:
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

    def extract_text(self):
        for page in self.extract_text_by_page():
            self.out_ptr.write(page)

"""
Please provide your brief explanation here.
Remove commented code
"""
            
class ExtractChunks():
    def __init__(self, text_path):
        self.chunks = []
        self.text_path = text_path
        self.text = ""

    def create_chunks(self):
        text_file_ptr = open(self.text_path)
        self.text = text_file_ptr.read()
        self.generate_titles()
        self.generate_para()
        self.generate_keywords()


    def generate_titles(self):
        table_of_content =  re.findall("[\w\s&\(\)]+\s\.+\s*\d+", self.text)
        for title in table_of_content:
            temp = Chunks()
            temp.set_title(title.split(".")[0].split(" ",1)[1])
            self.chunks.append(temp)

    def generate_para(self):
        chunk_len = len(self.chunks)
        content = self.text.split(self.chunks[chunk_len-1].title)
        for i in range(0,chunk_len-2):
            temp = self.chunks[i]
            para = re.findall(self.chunks[i].title+"[\w\s\W]+"+self.chunks[i+1].title, content[1])
            temp.set_para(" ".join(para))
        '''
        for chunk in self.chunks:
            print(chunk.title)
            print(chunk.para)
            print("\n")
        '''

    def generate_keywords(self):
        r = Rake()
        for chunk in self.chunks:
            text = chunk.para
            r.extract_keywords_from_text(text)
            chunk.set_keywords(r.get_ranked_phrases_with_scores())
        '''
        for chunk in self.chunks:
            print(chunk.title)
            print(chunk.para)
            print(chunk.keywords)
            print("\n\n")
        '''


"""
Add yout comments here for the class.
Try practicing making class attributes private to avoid external access. 
"""

class Chunks():
    def __init__(self):
        self.title = ""
        self.para = ""
        self.keywords= []
        
    def set_title(self, title):
        self.title = title
    
    def set_para(self, para):
        self.para = para
    
    def set_keywords(self, keywords):
        self.keywords = keywords
