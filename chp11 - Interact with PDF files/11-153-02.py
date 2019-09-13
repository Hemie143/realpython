import os
import copy
from PyPDF2 import PdfFileReader, PdfFileWriter

path = "./practice_files"
input_file_name = os.path.join(path, "Walrus.pdf")
input_file = PdfFileReader(open(input_file_name, "rb"))
output_PDF = PdfFileWriter()
input_file.decrypt('IamtheWalrus')

for page_num in range(0, input_file.getNumPages()):
    page_left = input_file.getPage(page_num)
    page_left.rotateClockwise(-90)
    page_right = copy.copy(page_left)
    # Get original page corner
    upper_right = page_left.mediaBox.upperRight
    # Crop and add left-side image
    page_left.mediaBox.upperRight = (upper_right[0]/2, upper_right[1])
    output_PDF.addPage(page_left)
    # Crop and add right-side image
    page_right.mediaBox.upperLeft = (upper_right[0]/2, upper_right[1])
    output_PDF.addPage(page_right)

# Add a password to the PDF file
output_file_name = os.path.join(path, "Output/New Walrus.pdf")
output_file = open(output_file_name, "wb")
output_PDF.write(output_file)
output_file.close()
