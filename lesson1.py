# Calculations, Printing, Variables

# Printing to the screen
# The built in function print(), prints to the screen
# it will print both Strings and numbers
print("Printing to the screen...")
print("Hello") # a string # double or single quotes ""
print('Hello again')
print(7) # print numbers
print("6") # a string again
print(6 +  6) # 12
print("6" + "6") # string concatenation
#print("6" + 6) # -> error

# Performing Calculations
# Operators
# Addition +
# Subtraction -
# Multiplication * 
# Division 
# Exponents **
# Modulo %

print(4 - 2) # Subtraction - 2
print(4 * 2) # multiplication -8
print(4 / 3) # division - 1.333
print("Modulo operator test...")
print(4**2)  # exponents - 64
print(5 % 3)
print(10 % 2)
print(16 % 3)
# Modulo gives remainders
# python operators follow the same order of operations as Math
print(4 - 2 * 2) # should give zero
print((4-2) * 2) # should give four

# variables 
# variables are used to hold data
# variables are declared and set to a value (initializing)
badLuck = 13 # declared a variable called badLuck and initialized it to 13
# i can print the variable using it's name 
print("badLuck = " + str(badLuck)) # cast it to a string
goodLuck = "4" # String variable 
print("goodLuck =" + goodLuck) # don't need to cast 


# you can also save input into variables
# using input(). A prompt goes inside the ()
name = input("What is your name? ")
print("Hello" + name)
print(name * 10)
name = name + "\n" # escape character (newline)
print(name * 10)
# MATH
base = input("Enter the base number: ")
exp = input("Enter the exponent: ")
print(int(base) ** int(exp))

