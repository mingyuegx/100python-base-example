if __name__=="__main__":
	N=10
	print("Please input ten numbers:")
	l=[]
	for i in range(N):
		l.append(int(input("Input a number:\n")))
		
	for i in range(N):
		print(l[i],end=" ")
		
	print()
	
	for i in range(N-1):
		min=i
		for j in range(i+1,N):
			if l[min]>l[j]:
				min=j
		k=l[i]
		l[i]=l[min]
		l[min]=k
	print()
	for i in range(N):
		print(l[i],end=" ")
		
	
