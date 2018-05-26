low=int(input("Input a min number:"))
upper=int(input("Input a max number:"))

for number in range (low,upper):
	if number>1:
		for i in range(2,number):
			if (number%i)==0:
				break
				
			
		else:
			print(number)
