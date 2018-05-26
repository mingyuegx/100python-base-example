
a=[]
tn=0
m=int (input("input a number:"))
n=int (input("input a number:"))
for count in range(m):
	tn=tn+n
	n=n*10
	a.append(tn)
	print(tn)
	
	
a=reduce(lambda x,y:x+y,a)
print (a)

