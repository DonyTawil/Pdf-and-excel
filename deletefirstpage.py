# This is a script to delete the final page in a pdf

import PyPDF2 as pdf

pdf1File = open('ANNEXE3.pdf', 'rb')


pdf1Reader = pdf.PdfFileReader(pdf1File)
pdfWriter = pdf.PdfFileWriter()

for pageNum in range(1,pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
	
pdfOutputFile = open('outputpdf.pdf','wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdf1File.close()