def hello_world():
	print('Hello World!')
	
def three_hellos():
	for i in range(3):
		hello_world()
		
if __name__=="__main__":
	three_hellos()
