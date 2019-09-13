import os
from PyPDF2 import PdfFileReader

path = "./practice_files"
input_file_name = os.path.join(path, "Pride and Prejudice.pdf")
input_file = PdfFileReader(open(input_file_name, "rb"))
print("Number of pages:", input_file.getNumPages())
print("Title:", input_file.getDocumentInfo().title)

