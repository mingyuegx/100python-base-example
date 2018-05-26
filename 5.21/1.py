a=[]
for i in range(1,5):
	for j in range(1,5):
		for k in range(1,5):
					if(i!=j)and (j!=k)and (i!=k):
						b=i*100+j*10+k
						a.append(b)
						
print(a)
