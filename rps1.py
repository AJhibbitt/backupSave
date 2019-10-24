# Austin Hibbitt
# Rock Paper Scissors Game
#_________________________
# break into pieces
# Welcome page, name entry
# Score screen with computer, player (name), tles
# Options or game r, p, s, q
# Game will loop until q is entered
# Each loop it will get a random choice from the computer
#a choice from the player, compare the two, and update score
# When game ends (q is entered) final score is displayed 

# Welcome page 
# Prompt for name
# a welcome message 

#_________________________

	# imports
import random
# variables
playerScore = 0
computerScore = 0
ties = 0
# make a list
cChoices =["r", "p", "s"]
print("Welcome to Rock Paper Scissors")
name = input("Enter your name: ")

while True:
	print("Score:")
print("Computer: " + str(computerScore))
print(name + ": " + str(playerScore))
print("Ties: " + str(ties))
choice = input("Enter 'r' for Rock, 'p' for Paper, 's' for Scissors or 'q' to quit: ")
computerChoice = random.choice(cChoices)
if choice == "q":
	break
if choice == "r":
print(name + " Picked Rock")
if computerChoice == "r": # Tie
print("Computer picked Rock")
print("This is a tie")
ties = ties + 1
elif computerChoice == "p":
print("Computer picked Paper")
print("Paper beats Rock")
computerScore += 1
else: # s is only choice left
print("Computer picked Scissors")
print("Rock beats Scissors")
playerScore += 1
elif choice == "p":
print(name + " Picked Paper")
if computerChoice == "r": # Tie
print("Computer picked Rock")
print("Paper covers Rock")
playerScore += 1
elif computerChoice == "p":
print("Computer picked Paper")
print("This is a Tie")
ties += 1
else: # s is only choice left
print("Computer picked Scissors")
print("Scissors cuts paper")
computerScore += 1
elif choice == "s":
print(name + " Picked Scissors")
if computerChoice == "r": # Tie
print("Computer picks Rock")
print("Rock breaks scissors")
computerScore += 1
elif computerChoice == "p":
print("Computer picked Paper")
print("Scissors cut paper")
playerScore += 1
else: # s is only choice left
print("Computer picked Scissors")
print("This is a tie")
ties += 1
else: #print type something else
print("That is not option")





    

