#
#Ethan Mackenzie Brown
#101031125
#
#Gaddis, T. (2015). "Starting Out With Python"

multipleParts = input("Does your symbol have multiple seperated parts? ")
isCurved = input("Does your symbol have curved lines, or is curved in any way? ")
pointsUp = input("Does an arrow in your symbol point up? ")
pointsDown = input("Does an arrow in your your symbol point down? ")
pointsLeft = input("Does an arrow in your your symbol point left? ")
pointsRight = input("Does an arrow in your your symbol point right? ")
ejectSymbol = input("Does your icon look like an eject symbol similar to one you wouold see on a dcd player? ")

if multipleParts.lower() == "yes" and isCurved.lower() == "yes" and pointsRight.lower() == "no":
	print("Your symbol is symbol 1")
elif multipleParts.lower() == "yes" and pointsUp.lower() == "yes" and pointsDown.lower() == "no":
	print("Your symbol is symbol 2")
elif pointsLeft.lower() == "yes" and isCurved.lower() == "yes" and pointsDown.lower() == "no":
	print("Your symbol is symbol 3")
elif multipleParts.lower() == "yes" and pointsRight.lower() == "yes" and pointsDown.lower() == "no":
	print("Your symbol is symbol 4")
elif pointsUp.lower() == "yes" and isCurved.lower() == "yes" and pointsDown.lower() == "no":
	print("Your symbol is symbol 5")
elif multipleParts.lower() == "yes" and pointsLeft.lower() == "yes" and pointsDown.lower() == "no":
	print("Your symbol is symbol 6")
elif isCurved.lower() == "yes" and pointsRight.lower() == "yes" and pointsDown.lower() == "no":
	print("Your symbol is symbol 7")
elif isCurved.lower() == "yes" and pointsDown.lower() == "yes" and ejectSymbol.lower() == "yes" and pointsDown.lower() == "no": 
	print("Your symbol is symbol 8")
elif multipleParts.lower() == "yes" and pointsUp.lower() == "yes" and pointsDown.lower() == "no":
	print("Your symbol is symbol 9")
elif pointsDown.lower() == "yes" and pointsUp.lower() == "yes" and pointsLeft.lower() == "no":
	print("Your symbol is symbol 10")
else:
	print("You have chosen a symbol not in the expert system or you have inputted an answer incorrectly (please be sure to type 'yes' or 'no' when answering the questions")