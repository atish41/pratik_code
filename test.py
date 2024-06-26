

import fitz
import pymupdf

#def extract_text_from_pdf(pdf_file):
 #   with pymupdf.open(pdf_file) as doc:
 #       text = ""
  #      for page in doc:
 #           text += page.get_text("text")  # Extract text from each page
 #       return text
def extract_text_from_pdf(pdf_bytes):
    with fitz.open(stream=pdf_bytes, filetype="pdf") as doc:
        text = ""
        for page in doc:
            text += page.get_text("text") # Extract text from each page
        return text