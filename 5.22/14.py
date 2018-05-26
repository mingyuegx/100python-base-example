
from sys import stdout
n=int(input("input number"))
print ("n=%d",n)

for i in range(2,n+1):
	while n!=i:
		if n%i==0:
			stdout.write(str(i))
			stdout.write(str("*"))
			n=int(n/i)
			
		else:
			break
print(n)
