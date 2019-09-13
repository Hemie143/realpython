import os
from PyPDF2 import PdfFileReader, PdfFileWriter

'''
2. Extract the full contents of The Whistling Gypsy.pdf into a .TXT file
3. Save a new version of The Whistling Gypsy.pdf that does not include the cover
page into the "Output" folder
'''

path = './practice_files'

input_file_name = os.path.join(path, 'The Whistling Gypsy.pdf')
input_file = PdfFileReader(open(input_file_name, 'rb'))

print("Title:", input_file.getDocumentInfo().title)
print("Author:", input_file.getDocumentInfo().author)
print("Number of pages:", input_file.getNumPages())

output_file_name = os.path.join(path, 'Output/The Whistling Gypsy.txt')
output_file = open(output_file_name, 'w', encoding="utf-8")
for page_num in range(0, input_file.getNumPages()):
    text = input_file.getPage(page_num).extractText()
    text = text.replace('  ', '\n')
    print(type(text))
    output_file.write(text)
output_file.close()

output_PDF = PdfFileWriter()
for page_num in range(1, input_file.getNumPages()):
    output_PDF.addPage(input_file.getPage(page_num))

output_file_name = os.path.join(path, 'Output/The Whistling Gypsy (no cover).pdf')
output_file = open(output_file_name, 'wb')
output_PDF.write(output_file)
output_file.close()
