from math import sqrt
from sys import stdout
a=[]
leap=True
for m in range(101,201):
	k=int(sqrt(m+1))
	for j in range(2,k+1):
		if (m%j)==0:
			leap=False
			break
	if leap==True:
		
		a.append(m)
	leap=True
		
		
print (a)
		
