year=int(input("year:\n"))
month=int(input("month:\n"))
day=int(input("day:\n"))
if (month>0 and month<=12 and day>0 and day<=31):
	pass
else:
	print("error")
	
months=(0,31,59,90,120,151,181,212,243,273,304,334)
sum=0
sum+=day
for i in range(1970,year):
	if (i%400==0 ) or (i%4==0 and i%100!=0):
		sum+=366
	else:
		sum+=365
if ((year%400==0 or (year%4==0 and year%100!=0))and month>2):
	
	for j in range(0,month):
		sum+=months[j]+1
else:
	for j in range(0,month):
		sum+=months[j]
		
print(sum)
	
	
