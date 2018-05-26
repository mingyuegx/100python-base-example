def output(s,l):
	if l==0:
		return
	print(s[l-1],end="")
	output(s,l-1)
	
s=str(input("Input a string:"))
l=len(s)
output(s,l)
