'''
This script helps to add water mark to any PDF's
which can have single page to multiple pages using PyPDF2 module
'''
'''
Intsall module using command 'pip install PyPDF2'
'''
import PyPDF2

# Initializing PDF file reader object for Source PDF
pdf_file_reader = PyPDF2.PdfFileReader(open('./PDF_Docs/give-and-take-BOOK.pdf','rb'))

# Initializing Water mark PDF file reader object which has only water mark in first page
watermark_file_reader = PyPDF2.PdfFileReader(open('./PDF_Docs/Confidential.pdf','rb'))

watermark = watermark_file_reader.getPage(0) #To get first page of the PDF which has water mark

writer = PyPDF2.PdfFileWriter()  #Initilaizes PDF writer object

for each_page in range(pdf_file_reader.getNumPages()):
    page = pdf_file_reader.getPage(each_page) # To each page in the PDF
    page.mergePage(watermark)  # Merges/Adds the water mark to each page
    writer.addPage(page)  # Writes the page to writer object

with open('./Processed_PDF_Docs/Book.pdf','wb') as file:
    writer.write(file) # Final pdf with water mark is stored here
