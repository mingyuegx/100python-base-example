from sys import stdout
if __name__=="__main__":
	filename=input("Input a filename\n")
	fp=open(filename,'w')
	ch=input("Input a str:\n")
	while ch!="#":
		fp.write(ch)
		stdout.write(ch)
		ch=input(' ')
		
	fp.close()
