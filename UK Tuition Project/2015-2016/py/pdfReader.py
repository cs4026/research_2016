import PyPDF2

alph={'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V'}
ints={'0','1','2','3','4','5','6','7','8','9'}
pdfFileObj=open('2016.pdf','rb')
pdfReader=PyPDF2.PdfFileReader(pdfFileObj)

#print(pdfReader.numPages)
f=open('f','r+')

pageObj=pdfReader.getPage(0)
f.write(pageObj.extractText())
f.close()
f=open('f','a+')
pageObj=pdfReader.getPage(1)
f.write(pageObj.extractText())
f.close
f=open('f','r')
w=open('qrs','w')
word=""
nextW=False
nextI=False
c=''
while True:
	c = f.read(1)
	for x in ints:
		if c==x:
			nextI=True
			nextW=False
	for x in alph:
		if c==x:
			nextW=True
	if not c:
		print ("End of file")
		break
	if c=="-":
		c="-"
	if nextW and nextI:
			w.write(word)
			print(word)
			w.write("\n")
			word=""
			nextw=False
			nextI=False

	word+=c
