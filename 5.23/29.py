x=int(input("Input a number:"))
y=str(x)
n=len(y)
print("It's %d number,"%n,end="\t")
for i in range(n-1,-1,-1):
	print(y[i],end="")


