import os
from PyPDF2 import PdfFileReader, PdfFileWriter

path = "./practice_files"
cover_file_name = os.path.join(path, "Emperor cover sheet.pdf")
cover_file = PdfFileReader(open(cover_file_name, "rb"))
content_file_name = os.path.join(path, "The Emperor.pdf")
content_file = PdfFileReader(open(content_file_name, "rb"))
output_PDF = PdfFileWriter()

for page_num in range(0, cover_file.getNumPages()):
    page = cover_file.getPage(page_num)
    output_PDF.addPage(page)

for page_num in range(0, content_file.getNumPages()):
    page = content_file.getPage(page_num)
    output_PDF.addPage(page)

output_file_name = os.path.join(path, "Output/The Covered Emperor.pdf")
output_file = open(output_file_name, "wb")
output_PDF.write(output_file)
output_file.close()