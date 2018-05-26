f1=1
f2=1
a=[1,1]
m=int(input("input month:"))


for i in range(3,m+1):
	
	j=a[i-3]+a[i-2]
	a.append(j)
	
print(a[m-1])
	
	
	
