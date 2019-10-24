print("Welcome to your To Do List.")
todoList= ["MATH", "BIOLOGY", "ENGLISH"]
while True:
	print("Enter a to add item")
	print("Enter r to remove item")
	print("Enter p to print list")
	print("Enter q to quit")
	choice = input("Choose: ")

	if choice == "q":
		break
	elif choice == "a":
		aDD= input("What would you like to add? ")
		todoList.append(aDD)
		print(todoList)
		# add item to list
		pass
	elif choice == "r":
		print(todoList)
		re = input("What would you like to remove? ")
		if re == "r":
			todoList.remove("r")
			print(todoList)
			if re == "Math":
				todoList.remove("MATH")


		pass
	else:
		print("You chose something unlisted. Try again.")