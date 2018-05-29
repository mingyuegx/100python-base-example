def decall(n,number=1):
	sum=0
	if (number==1):
		for i in range(1,int(n/2+1)):
			sum+=1/(2*i)
			
	else:
		for i in range(1,n,2):
			sum+=(1/i)
	return(sum)
		









if __name__=="__main__":
	n=int(input("Input a number:\n"))
	if(n%2==0):
		sum=decall(n,1)
	else:
		sum=decall(n,2)
		
	print(sum)
