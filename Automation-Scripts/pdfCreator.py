#! python3
import PyPDF2
# Creating dict in order to gather all info at one place 
pdf={}
# Nmber of PDF files are requre to make new pdf
numPdf = input('Type number of PDF files you want to copy in a new PDF : ')
for i in range(numPdf):
               # Sequence or order of PDF files in new a new pdf file
               b=input('Type sequence of this Pdf you want in a new Pdf in numeric order : ')
               """if b in seq:
                   print('This sequence already exist. Try new sequence...')
                   i = i
                   continue
                elif b>numPdf:
                    print('Sequence order is out of range. Try another...')
                    i=i
                continue"""
               a=raw_input('Type Pdf name if it is in same folder : ')
               print('Number of pages you want to copy from this pdf ')
               s=input('Type Starting Page Number you want and page number starts from 1 : ')
               e= input('Type Last Page Number you want : ')
               pdf.setdefault(b, {})
               pdf[b].setdefault(a, {'start':s-1, 'end':e-1})
writingPdf=PyPDF2.PdfFileWriter()              
for i in range(1, numPdf+1):
  for k in pdf[i].keys():
    openPdf=open(k, 'rb')
    readingPdf=PyPDF2.PdfFileReader(openPdf)

    for t in range(pdf[i][k]['start'], pdf[i][k]['end']+1):
        copyPdf=readingPdf.getPage(t)
        writingPdf.addPage(copyPdf)

newPdf=open('new_Pdf.pdf', 'wb')
writingPdf.write(newPdf)
newPdf.close()
"""for l in range (numPdf):
   pdf[bi].keys().close()
"""    
