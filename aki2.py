#!/usr/bin/python3
import random
count=0
r=0
while count<=100:
	roll=input("press r to roll the dice :")
	if roll=="r":
		r=random.randint(1,6)
		count=count+r
		print("your random num is",r)
		print("you are on count",count)

		if count>=100:
			print("well done")
		elif count==13:
			print("climb ladder to 34")
			count=34
		elif count==11:
			print("go back to 2")
			count=2
		elif count==8:
			print("climb ladder to 37")
			count=37
		elif count==25:
			print("go back to 4")
			count=4
		elif count==38:
			print("go back to 9")
			count=9	
		elif count==40:
			print("climb ladder to 68")
			count=68
		elif count==65:
			print("go back to 46")
			count=46
		elif count==52:
			print("climb ladder to 81")
			count=81
		elif count==76:
			print("climb ladder to 97")
			count=97
		elif count==89:
			print("go back to 70")
			count=70
		elif count==93:
			print("go back to 64")
			count=64
		elif count==100:
			print("VICTORY!!")
			count=100
		

	