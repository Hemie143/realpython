import os
from PyPDF2 import PdfFileReader

path = './practice_files'

input_file_name = os.path.join(path, 'Pride and Prejudice.pdf')
input_file = PdfFileReader(open(input_file_name, 'rb'))

output_file_name = os.path.join(path, 'Output/Pride and Prejudice.txt')
output_file = open(output_file_name, 'w')

title = input_file.getDocumentInfo().title
total_pages = input_file.getNumPages()

output_file.write(title + '\n')
output_file.write('Number of pages: {}\n\n'.format(total_pages))

for page_num in range(0, total_pages):
    text = input_file.getPage(page_num).extractText()
    text = text.replace('  ', '\n')
    output_file.write(text)

output_file.close()
