#_*_ coding:UTF-8 _*_

for n in range(100,1000):
	i=int(n/100)
	j=int(n/10%10)
	k=int(n%10)
	if n==i*i*i + j*j*j + k*k*k:
		print(n)


	
