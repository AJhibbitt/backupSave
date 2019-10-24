# This is a check/review to make sure nothing was "lost" over break

# Austin Hibbitt
# Period 1

# Variable declaration and assigntment(s)
# Example: 
myVar = "hello"
# Declare two variables; 1 string, 1 number, and assign values
myNum = 4

# While loop
# Example:
# As long as x is zero, it will continue
x = 10
while x > 0:
	print(x)
	x = x -1

# Print name 100 times

x = 100
while x > 0:
	print("austin")
	x = x -1

# String Concatenation
# Example: 
name = "austin"
print("Hello " + name + ", how are you")
# make a variable with your favorite movie
favMovie = "Pulp Fiction"
print("My favorite movie is " + favMovie)

# input - will wait for an answer 
# Example: 
myName = input("What is your name?: ")
print("Your name is: " + myName)
# prompt for favorite song and print "your favorite song is: "
mySong = input("What is your favorite song: ")


#casting: Changing the type of a variable 
#myNum = 40 
#print("My number is " + str(myNum))
#num1 = input("Enter a number: ")
#num1 = int(num1) + 10:
#print("num1 + 10 is " + str(num1))

# ask for two numbers, add them and print
numBer = input("Type number:")
nuMber = input("Type another:")
anS = numBer + nuMber
input("Your number is: " + anS)

#"if" and "else"
# example 
num1 = int(input("Type a number: ")) 
if num1 > 100:
	print("Your number is more than 100.")
elif num1 == 100:
	print("Number is EQUAL to 100!")
else: 
	print("Your number is less than or equal to 100.")

# ask if birthday is today 

ques = int(input("Is it your birthday today? ")
if ques == "yes":
	print("Happy Birthday!")
else: 
	print("Oh well nevermind then")
