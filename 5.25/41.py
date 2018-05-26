def varfunc():
	var=0
	print("var=%d"%var)
	var+=1

if __name__=="__main__":
	for i in range(3):
		varfunc()


class static:
	StaticVar=5
	def varfunc(self):
		self.StaticVar+=1
		print(self.StaticVar)
		
print(static.StaticVar)

a=static()
for i in range(3):
	a.varfunc()
