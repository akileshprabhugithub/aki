#!/usr/bin/python3
from random import randint

#create a list of play options
t = ["rock", "paper", "scissors", "lizard", "spock"]
cc=0
pc=0
#assign a random play to the computer
computer = t[randint(0,4)]
 
#set player to False
player = False
 
while player == False:
#set player to True
	player = input("rock ,paper ,scissors ,lizard ,spock")
	if player == computer:
		print("Tie!")
	elif player == "rock":
		if (computer == "paper"or computer == "spock"):
			print("You lose!", computer, "covers/vapourizes", player)
			cc=cc+1
			print("ur score is",pc,"comp score is",cc)    
		else:
			print("You win!", player, "smashes/crushes", computer)
			pc=pc+1
			print("ur score is",pc,",comp score is",cc) 
	elif player == "paper":
		if (computer == "scissors"or computer == "lizard"):
			print("You lose!", computer, "cut/eats", player)
			cc=cc+1
			print("ur score is",pc,",comp score is",cc) 
		else:
			print("You win!", player, "covers/disproves", computer)
			pc=pc+1
			print("ur score is",pc,",comp score is",cc) 
	elif player == "lizard":
		if (computer == "rock"or computer == "scissors"):
			print("You lose!", computer, "crushes/dicapitates", player)
			cc=cc+1
			print("ur score is",pc,",comp score is",cc) 
		else:
			print("You win!", player, "poisons/eats", computer)
			pc=pc+1
			print("ur score is",pc,",comp score is",cc) 
	elif player == "spock":
		if (computer == "paper"or computer == "lizard"):
			print("You lose!", computer, "poisons/disproves", player)
			cc=cc+1
			print("ur score is",pc,",comp score is",cc) 
		else:
			print("You win!", player, "vapourizes/smashes", computer)
			pc=pc+1
			print("ur score is",pc,",comp score is",cc) 
	elif player == "scissors":
		if (computer == "rock"or computer == "spock"):
			print("You lose!", computer, "crushes/smashes", player)
			cc=cc+1
			print("ur score is",pc,",comp score is",cc) 
		else:
			print("You win!", player, "cuts/dicapitates", computer)
			pc=pc+1
			print("ur score is",pc,",comp score is",cc) 
	else:
		print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
	player = False
	computer = t[randint(0,4)]