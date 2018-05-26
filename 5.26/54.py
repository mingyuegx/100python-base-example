if __name__=="__main__":
	a=int(input("Input a number:"))
	b=a>>4
	c=~(~0<<4)
	d=b&c
	print("%d\t%d"%(a,d))
