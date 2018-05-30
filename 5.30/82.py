if __name__=="__main__":
	n=0
	p=input("Input a number:")
	for i in range(len(p)):
		n=n*8+ord(p[i])-ord('0')
		
	print(n)
