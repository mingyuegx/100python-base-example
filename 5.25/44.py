X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
 
Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]
    
result=[[],[],[]]
 
for i in range(len(X)):
	 for j in range(len(X[0])):
		 result[i].append(X[i][j]+Y[i][j])
		 
for r in result:
	print(r)

