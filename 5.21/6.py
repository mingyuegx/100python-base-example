a=[0,1]
i=int(input("i="))
for i in range(2,i+1):
	y=a[i-1]+a[i-2]
	a.append(y)
print(a[i])
print (a)
