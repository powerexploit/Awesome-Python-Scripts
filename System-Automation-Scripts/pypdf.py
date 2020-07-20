#!/usrbin/python3
# Automation with pdf file
# Script design just to automate stuffs with pdf file
import PyPDF2
import os
print(os.system('pyfiglet pypdf'))
pdFileObj = open('Exam-Transcript.pdf','rb')
#open pdf file in read binary mode(rb) & store in pdfFileObj
pdfReader = PyPDF2.PdfFileReader(pdFileObj)
#pdfFileReader represents pdf file
print(pdfReader.numPages)
#to check number of pages in you pdf file use .numPages()
pageObj = pdfReader.getPage(0)
print(pageObj.extractText()) #extract the pdf data in text format
