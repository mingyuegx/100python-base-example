if __name__=="__main__":
	n=1
	while n<=7:
		a=int (input("Input a number:\n"))
		while a<1 or a>50:
			a=int(input("Input a number:\n"))
			
		print(a*'*')
		n+=1
