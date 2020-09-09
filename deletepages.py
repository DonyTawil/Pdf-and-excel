# This is a script to delete the final page in a pdf

import PyPDF2 as pdf

pdf1File = open('ANNEXE2.pdf', 'rb')


pdf1Reader = pdf.PdfFileReader(pdf1File)
pdfWriter = pdf.PdfFileWriter()

pages = [i for i in range(202, 208)]   #Pour pages entre 202 et 207 (le dernier numero n' est pas pris en compte

for pageNum in range(pdf1Reader.numPages):
    if (pageNum + 1) in pages:
	    continue
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
	
pdfOutputFile = open('outputpdf.pdf','wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdf1File.close()