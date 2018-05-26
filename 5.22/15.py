score=int (input("please input score:"))
grade==(score>=90)?"A":"B"
	
if score<=89 and score>=60:
	grade="B"
else:
	grade="C"
	
print (" %d belongs to %s"%(score,grade))
