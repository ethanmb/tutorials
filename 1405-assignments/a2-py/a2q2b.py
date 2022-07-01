#
#Ethan Mackenzie Brown
#101031125
#
#Gaddis, T. (2015). "Starting Out With Python"

userInput = int(input("How many parts does your symbol have? "))

if userInput > 1:
	if userInput == 2:
		userInput = input("Does your symbol look like and eject symbol similar to one found on a dvd player? ")
		if userInput.lower() == "yes":
			print("You have chosen symbol number 9")
		else:
			print("You have chosen symbol number 2")
	if userInput == 3:
		userInput = input("Does your symbol have an arrow that points right? ")
		if userInput.lower() == "yes":
			print("You have chosen symbol number 4")
		else:
			print("You have chosen symbol number 1")
	if userInput == 4:
		print("You have chosen symbol number 6")
else:
	userInput = input("Which direction(s) does your symbol point? ")
	if userInput.lower() == "up":
		print("You have chosen symbol number 5")
	elif userInput.lower() == "down":
		print("You have chosen symbol number 8")
	elif userInput.lower() == "left":
		print("You have chosen symbol number 3")
	elif userInput.lower() == "right":
		print("You have chosen symbol number 7")
	else:
		print("You have chosen symbol number 10")