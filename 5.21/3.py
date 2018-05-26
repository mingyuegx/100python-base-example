#_*_coding:UTF-8 _*_
import math
a=[]

for i in range(0,10000):
	x=int(math.sqrt(i+100))
	y=int(math.sqrt(i+268))
	if (x**2==i+100)and (y**2==i+268):
		a.append(i)
print(a)
		
