student=[]
for i in range(3):
	student.append(['','',[]])
	
	
def input_stu(stu):
	for i in range(3):
		stu[i][0]=input("Input student num:\n")
		stu[i][1]=input("Input student name:\n")
		for j in range(3):
			stu[i][2].append(int(input("score:")))
			
			
			
def output_stu(stu):
	for i in range (3):
		print("%-6s%-10s"%(stu[i][0],stu[i][1]))
		for j in range(3):
			print("%-8d"%int(stu[i][2][j]))
			
if __name__=="__main__":
	input_stu(student)
	print(student)
	output_stu(student)
