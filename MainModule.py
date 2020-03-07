import argparse

from PDFToTextModule import PDFToText

from PDFToTextModule import ExtractChunks

# @Fiza - Kindly convert this utility into class PDFParser


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Enter document filename")
    parser.add_argument('doc', help='document filename')
    args = parser.parse_args()
    f_name = args.doc  # input document filename
    print(f_name)
    pdf_to_text = PDFToText(f_name)
    pdf_to_text.extract_text()
    extract_chunk = ExtractChunks(pdf_to_text.text_path)
    extract_chunk.create_chunks()

