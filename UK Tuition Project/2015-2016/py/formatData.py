f=open("grad",'r')
fn=open("grad new",'w')

word=""
c=""
sCount=0
while True:
	c=f.read(1)
	if not c:
		print("End of File")
		break
	else:
		if c==" " and sCount==1:
			fn.write(word)
			fn.write("\n")
			word=""
			sCount=0
		elif c==" ":
			sCount+=1
			word+=c
		else:
			word+=c

