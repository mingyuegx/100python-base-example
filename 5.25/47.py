def exchange(x,y):
	n=x
	x=y
	y=n
	return(x,y)
	
if __name__=="__main__":
	x=int(input("Input a number"))
	y=int(input("Input anthor number"))
	print("x=%d,y=%d"%(x,y))
	x,y=exchange(x,y)
	print("x=%d,y=%d"%(x,y))

