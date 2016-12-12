f=open('grad new','r')

c=0
count=0
word=""
while True:
	r=f.read(1)
	if not r:
		print("EOF")
		break
	if r==" " and count==1:
		print(word)
		word=""
		c+=1
		count=0
	elif r==" " and count==0:
		word+=r
		count+=1
	else:
		word+=r
