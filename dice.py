# Austin Hibbitt
# Period 1
# Dice Rolling Simulator
import random
nuM = int(input("Enter a number of rolls: "))
cChoice = random.randint(1, 6)
if nuM == cChoice:
	for x in range(100):
		print(random.choice(cChoice))
if cChoice ==1 : 
	print("Rolled 1")
elif cChoice==2: 
	print("Rolled 2")
elif cChoice==3: 
	print("Rolled 3")
elif cChoice==4:
    print("Rolled 4")
elif cChoice==5:
    print("Rolled 5")
elif cChoice==6:
    print("Rolled 6")
