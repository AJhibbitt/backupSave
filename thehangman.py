import random 
wordList = ["car", "money", "japan","trance", "ice", "fresh","wolf", "falcon", "marshmello", "russia",]
raN = [ran1, ran2, ran3, ran4, ran5, ran6, ran7, ran8, ran9, ran10]
word = random.choice(wordList)

while True:
 letter = input("Enter a letter: ")
 if letter in word:
	print("Letter is in word! ")
else:
	print("Letter is not in the word. Try again! ")
count = 0 

for letter2 in word:
	if letter2 == letter:
		print(count)
	count +=1
else: 
	print(count)
	count -=1