#!/usr/bin/python3
#assigning random play to the computer
import random
count=0
r=0
while count<=100:
#while loop runs only when the above condition is satisfied	
	roll=input("press r to roll the dice")
#assigning roll equals to input performing the action of rolling the dice
	if roll=="r":
#this if statement will work as long as the given input is r
		r=random.randint(1,6)
#assign a random play to the computer
		count=count+r
		print("your random num is",r)
		print("you are on count",count)
