
import time
if __name__=="__main__":
	start=time.ctime(time.time())
	for i in range(3000):
		print(i)
	end=time.ctime(time.time())
	
	
	print("start time:%s \n end time:%s"%(start,end))
