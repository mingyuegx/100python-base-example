a=int (input("Input a number:"))
x=str(a)
flag=True

for i in range(int(len(x)/2)):
	if x[i]!=x[-i-1]:
		flag=False
		break
		
if flag:
	print("%d is a hui number"%a)
	
else:
	print("%d is not a hui number"%a)

