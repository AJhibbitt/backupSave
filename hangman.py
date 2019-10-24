import random 
import sys 

name = input("What is your name? ")
print("Hello", str(name), ("Welcome to Hangman, Good luck"))

while True:
	woRds = ["car", "money", "japan","trance", "ice","fresh","wolf", "falcon", "marshmello", "russia",]

length = len(secretWord)
guessWord= []
letterZ= []
secretWord = random.choice(woRds)

while True:
	for character in secretWord:
		guessWord.append("_")
		print("LETTER HAS", length, "WORDS. JUST TO LET YOU KNOW!")
		print(guessWord)
def guess():
	guesses= 0
	while guesses < 10
#myWord = "hello"

#choice = input("Type a word: ")

#@if choice == myWord:
	#print("It's a match")
#@print("Not a match. Try again!")

#letter = input("Enter a letter: ")

#if letter in myWord:
	#print("Letter is in word")
#else: 
	#@print("Letter is not in word. Try again ")

#count = 0 
#myList = list(myWord)
#for letter2 in myList:
	#if letter2 == choice:
		#print(count)
	#count += 1

#guess = input("Guess a letter: ")
#if guess in secretWord:
#print("Letter in word")
#else : misses= misses + 1

#print(mISS"L +_str(misses))