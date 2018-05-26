if __name__=="__main__":
	a=[1,4,5,6,8,12,34,56,78,90,0]
	print(a)
	number=int(input("Input a number:"))
	n=len(a)-1
	if number>a[n-1]:
		a[n]=number
	else:
		for i in range(n):
			if a[i]>number:
				temp1=a[i]
				a[i]=number
				for j in range(i+1,n+1):
					temp2=a[j]
					a[j]=temp1
					temp1=temp2
				break
					
	for i in range(n+1):
		print(a[i])
				
