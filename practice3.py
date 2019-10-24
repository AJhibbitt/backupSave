nuM = input("Enter a number of rolls: ")
x = random.randint(1, 6)
print(x) numRolls = int(input("How many rolls: "))
import random

while True:
    rolled_num = random.randint(1,6)
    print("The dice rolled and you got: ", rolled_num)
    input("Press any key to roll again.")



    st = 1
stt = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
	print("Rolling the dices")
	print("The values are..")
	print(random.randint(st, stt))
	print(random.randint(st, stt))

	roll_again = raw_input("Roll the dices again? ")

	
	
	
	