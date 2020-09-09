import PyPDF2 as pdf

pdf_to_merge = ["ECO-213-102-J-BPO0", "ANNEXES"]

pdfWriter = pdf.PdfFileWriter()

for dapdf in pdf_to_merge:
    #open the pdf
	pdfFile = open(dapdf + ".pdf", 'rb')
	pdfReader = pdf.PdfFileReader(pdfFile)
	
	#loop through all the pages
	for pageNum in range(pdfReader.numPages):
		pageObj = pdfReader.getPage(pageNum)
		pdfWriter.addPage(pageObj)
		

pdfOutputFile = open('outputpdf.pdf','wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()

