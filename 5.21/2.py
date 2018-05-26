i=int(input("lirui:"))
arr=[100000,60000,40000,20000,10000,0]
rat=[0.01,0.015,0.03,0.05,0.075,0.1]

if(i<0):
	print("error")
r=0
for index in range(0,6):
	if i>arr[index]:
		r+=(i-arr[index])*rat[index]
		i=arr[index]
		
print (r)
	

