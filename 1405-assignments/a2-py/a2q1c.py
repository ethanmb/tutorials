#
#Ethan Mackenzie Brown
#101031125
#
#Gaddis, T. (2015). "Starting Out With Python"

userInput = input("Does your face have a moustache? ")

if userInput.lower() == "yes":
	userInput = input("Does your face have a wig? ")
	if userInput.lower() == "yes":
		print("You have chosen face number 18")
	else:
		print("You're face is number: 6, 10, 13, or 15")
else:
	print("You have not chosen faces number: 6, 10, 13, 15, or 18")
print("Thanks for playing")