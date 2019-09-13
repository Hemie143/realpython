import os
from PyPDF2 import PdfFileReader, PdfFileWriter

path = "./practice_files"
input_file_name = os.path.join(path, "ugly.pdf")
input_file = PdfFileReader(open(input_file_name, "rb"))
output_PDF = PdfFileWriter()

for page_num in range(0, input_file.getNumPages()):
    page = input_file.getPage(page_num)
    if page_num % 2 == 0:
        page.rotateClockwise(90)
    output_PDF.addPage(page)

output_file_name = os.path.join(path, "Output/The Conformed Duckling.pdf")
output_file = open(output_file_name, "wb")
output_PDF.write(output_file)
output_file.close()