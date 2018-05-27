p=0
def arr_max(array):
	max=0
	for i in range(1,len(array)):
		p=i
		if array[p]>array[max]:
			max=p
			
		k=max
		array[0],array[k]=array[k],array[0]
		
def arr_min(array):
	min=0
	for i in range(1,len(array)):
		p=i
		if array[p]<array[min]:
			min=p
	l=min
	array[5],array[1]=array[1],array[5]


if __name__=="__main__":
	array=[]
	number=int (input("input a number:"))
	for i in range (0,number):
		array.append(int (input("Input a number:")))
	arr_max(array)
	arr_min(array)
	print("computer result:")
	
	for i in range (len(array)):
		print(array[i])
		
	
