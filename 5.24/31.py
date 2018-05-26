#!/usr/bin/python
# -*- coding: UTF-8 -*-
while True:
	letter = input("please input:")
	if letter=="quit":
		break
	#while letter  != 'Y':
	if letter == 'S':
		print ('please input second letter:')
		letter = input("please input:")
		if letter == 'a':
			print ('Saturday')
		elif letter  == 'u':
			print ('Sunday')
		else:
			print ('data error')
		
	elif letter == 'F':
		print ('Friday')
		
	elif letter == 'M':
		print ('Monday')
		
	elif letter == 'T':
		print ('please input second letter')
		letter = input("please input:")
	 
		if letter  == 'u':
			print ('Tuesday')
		elif letter  == 'h':
			print ('Thursday')
		else:
			print ('data error')
			
	elif letter == 'W':
		print ('Wednesday')
	else:
		print ('data error')
