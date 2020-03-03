from io import StringIO


from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

import fitz
import argparse

import time

def extract_text_by_page(pdf_path):
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


def extract_text(pdf_path, pdf_file_ptr):
    for page in extract_text_by_page(pdf_path):
        pdf_file_ptr.write(page)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Enter document filename")
    parser.add_argument('doc', help='document filename')
    args = parser.parse_args()
    fname = args.doc  # input document filename
    print (fname)
    fname1 = 'SampleText/'+fname[:-4] + '-text.txt'
    print (fname1)
    outf = open(fname1, "w")

    extract_text('SamplePdf/'+fname, outf)

