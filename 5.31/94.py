import time
import random


if __name__=="__main__":
	play_it=input("do you want to play it.(\'y\'or\'n\')")
	while play_it=='y':
		c=input("Input a character:\n")
		i=random.randint(0,2**32)%100
		print("please input number you guess:\n")
		start=time.clock()
		a=time.time()
		guess=int(input("Input your guess\n"))
		while guess!=i:
			if guess>i:
				print("please input a litter smaller")
				guess=int(input("Input you guess:\n"))
			else:
				print("please input a litter bigger")
				guess=int (input("Input your guess:\n"))
				
		end=time.clock()
		b=time.time()
		var=(end-start)/18.2
		print(var)
		if var<15:
			print("you are very clever")
			
		elif var<25:
			print("you are normal")
		else:
			print("you are stupid")
			
		print("congradulations")
		print("The number you guess is %d"%i)
		play_it=input("do you want to play it")
			
	
	
