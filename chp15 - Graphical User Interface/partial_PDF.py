from easygui import *
from PyPDF2 import PdfFileReader, PdfFileWriter

input_file_name = fileopenbox("", "Select a PDF file...", "*.pdf")
if input_file_name is None:
    exit()

input_file = PdfFileReader(open(input_file_name, "rb"))
total_pages = input_file.getNumPages()
page_start = enterbox("Enter the number of the start page:", "Start page")
if page_start is None:
    exit()
while (not page_start.isdigit() or not (1 <= int(page_start) <= total_pages)):
    msgbox("Please provide a valid page number.", "")
    page_start = enterbox("Enter the number of the start page:", "Start page")
    if page_start is None:
        exit()

page_end = enterbox("Enter the number of the end page:", "End page")
if page_end is None:
    exit()

while (not page_end.isdigit() or not (1 <= int(page_start) <= total_pages)
        or int(page_end) < int(page_start)):
    msgbox("Please provide a valid page number.", "")
    page_end = enterbox("Enter the number of the end page:", "End page")
    if page_end is None:
        exit()

output_file_name = filesavebox("", "Save the trimmed PDF as...", "*.pdf")
while input_file_name == output_file_name:
    msgbox("Cannot overwrite original file!", "Please choose another file...")
    output_file_name = filesavebox("", "Save the trimmed PDF as...", "*.pdf")
if output_file_name is None:
    exit()

output_PDF = PdfFileWriter()
for page_num in range(int(page_start) - 1, int(page_end)):
    output_PDF.addPage(input_file.getPage(page_num))

output_file = open(output_file_name, "wb")
output_PDF.write(output_file)
output_file.close()
