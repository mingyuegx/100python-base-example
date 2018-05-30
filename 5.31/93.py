import time
if __name__=="__main__":
	start=time.clock()
	for i in range(10000):
		print(i)
	
	end=time.clock()
	print(start,end)
	print("different is %6.3f"%(end-start))
	
	
	
