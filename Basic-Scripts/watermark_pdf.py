'''
This script helps to add water mark to any PDF's
which can have single page to multiple pages using PyPDF2 module
'''
'''
Intsall module using command 'pip install PyPDF2'
'''
import PyPDF2

SOURCE_PDF      = "<PROVIDE THE SOURCE PDF PATH HERE >"
WATERMARK_PDF   = "< PROVIDE THE WATERMARK PDF PATH HERE >"
DESTINATION_PDF = "< PROVIDE THE DESTINATION PATH HERE FOR STORING FINAL PDF >"

# Initializing PDF file reader object for Source PDF
pdf_file_reader = PyPDF2.PdfFileReader(open(SOURCE_PDF,'rb'))

# Initializing Water mark PDF file reader object which has only Water mark in first page
watermark_file_reader = PyPDF2.PdfFileReader(open(WATERMARK_PDF,'rb'))

watermark = watermark_file_reader.getPage(0) #To get first page of the PDF which has water mark

writer = PyPDF2.PdfFileWriter()  #Initilaizes PDF writer object

for each_page in range(pdf_file_reader.getNumPages()):
    page = pdf_file_reader.getPage(each_page) # To get each page in the PDF
    page.mergePage(watermark)  # Merges/Adds the water mark to each page
    writer.addPage(page)  # Writes the page to writer object

with open(DESTINATION_PDF,'wb') as file:
    writer.write(file) # Final pdf with water mark is stored in destination path
