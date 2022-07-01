#
#Ethan Mackenzie Brown
#101031125
#
#Gaddis, T. (2015). "Starting Out With Python"

#fuction to create dictionary based off of file given
def createDictionary():
	#opens file
	x = open("your-assigned-glyphs.dat")
	#assigns file to variable
	string1 = x.read()
	#closes file
	x = x.close()
	#removes beginning and end junk in string
	string1 = string1.strip("%.:")
	#creates an array splt at '.'
	list_string = string1.split(".")
	#creates empty dictionary
	dictHomo = {}
	#loop to set keys and values. Since with the file given, only one value is assigned to each key
	#value is put into a list to make life easier in upcoming functions
	for x in range(0, len(list_string), 2):
		dictHomo[list_string[x]] = [list_string[x+1]]
	return dictHomo
	
#function that translates inputted string into homoglyphs in given file	
def myTranslate(dict, string_in):
	for x in dict:
		#makes sure key in dictionary is in string inputted
		if string_in.find(x) > -1:
			#loop to replace case of key with value, looped so if there are multiple occurances
			for y in range(len(string_in)):
				if x == string_in[y]:
					string_in = string_in[:y] + dict[x][0] + string_in[y + 1:]
	return string_in
	
#fuction that counts amount of values at inputted key
def myCount(dict, string_in):
	if string_in in dict:
		return len(dict[string_in])
	else:
		return 0
		
#function to remove a value at a key if that key contains more than one value.
#deletes entire key if there is only one value at inputted key
#returns 0 if user inputs a key that doesn't exist, or a value that doesn't exist at inputted key. Makes logical sense to user either way
def myRemove(dict, key, value):
	if key in dict:
		if value in dict[key]:
			if len(dict[key]) > 1:
				dict[key].remove(value)
				return len(dict[key])
			else:
				del dict[key]
				return 0
		else:
			return 0
	else:
		return 0
			
def main():
	userIn = input("Would you like to: 'quit', 'translate', 'count', or 'remove'? ")
	if userIn == "quit":
		exit()
	elif userIn == "translate":
		stringTrans = input("Input what you would like to translate: ")
		print(myTranslate(dictionary1, stringTrans))
	elif userIn == "count":
		stringToCheck = input("Input the string argument that will be checked in the dictionary at that key: ")
		print(myCount(dictionary1, stringToCheck))
	elif userIn == "remove":
		stringKey = input("Input the key that you would like to check at: ")
		stringValue = input("Input the value that you would like removed: ")
		print(myRemove(dictionary1, stringKey, stringValue))
	else:
		print("Incorrect input, try again.")
		#calls function again if input is incorrect
		main()
		

		
dictionary1 = createDictionary()
#program will loop infinitely unless told to quit by user in main()
while True:
	main()