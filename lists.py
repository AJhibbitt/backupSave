favFood = ["Steak", "Rice", "Ribs"]
print(favFood[0])
print(favFood[1])
print(favFood)
# Adds to the end of the list 
favFood.append("Chicken")
print(favFood)
print("My fourth favorite food is " + favFood[3])
# insert - adds to an index in a list 
favFood.insert(1, "Ramen")
print(favFood)
# remove item from list
favFood.remove("Chicken")
print(favFood)
# remove by index
favFood.pop(0)
print(favFood)

favFood.insert(0, "Steak")
#loop through list 
for food in favFood:
	print(food)

numList = [8, 6, 7, 5, 3, 0, 9, 9]

# Loop through list and add all the numbers together then print the sum

sum = 0
for num in numList:
	sum= sum + num
print(sum)

# function to get length of list
print(len(numList))

# make a list for favorite movies
# prompt for a favorite movie
myMovie = ["Who Killed Captain Alex? ", "Godfather", "Man with No Name Trilogy"]
favMov = input("What is your favorite movie? ")
myMovie.append(favMov)
print(myMovie)
myMovie.remove("<<")
print(myMovie)

# List methods and functions
# append - adds an item t0 the end of a list
# insert - adds an item to a specified index
# remove - removes a specified item from a list
# pop - removes an item from a specified idex
# len - returns the length of a list
