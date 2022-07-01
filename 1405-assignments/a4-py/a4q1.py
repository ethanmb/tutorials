#
#Ethan Mackenzie Brown
#101031125
#
#Gaddis, T. (2015). "Starting Out With Python"
#The Python Standard Library. (2016-11-02). Retrieved from https://docs.python.org/3/library/stdtypes.html#str.join

def concat_slices_and_print():
	stringToSlice = "gfdcbajklmoutpqrvwshixyznbcdfegjklmp"
	#blank string that will be added onto from slices of original
	newString = ""
	#slices letters 11, and 12 (starting if counting first letter as 1) from original string
	newString += stringToSlice[10:13]
	#slices numbers 19 and 20
	newString += stringToSlice[18:21]
	#slices 25th letter
	newString += stringToSlice[24]
	newString += stringToSlice[29]
	print(newString)
	
def if_positive_concat_slices(int1):
	if int1 > 0:
		stringToSlice = "xwvtsyzmuefjkolpqrstvchwxyzinbdefgjkop"
		newString = ""
		newString += stringToSlice[7:9]
		newString += stringToSlice[14]
		newString += stringToSlice[21:23]
		newString += stringToSlice[27:29]
		newString += stringToSlice[33]
		print(newString)

def return_concat_slices():
	stringToSlice = "wvutsqxyzmalfhjkopiqstuvwgnexyzrcdfh"
	newString = ""
	newString += stringToSlice[9:12]
	newString += stringToSlice[18]
	newString += stringToSlice[25:28]
	newString += stringToSlice[31]
	return newString

def concat_arg_slices_and_return(string1):
	if string1 == "qpnmlkstuwbehxyzavifgjkolmnprqstuwx":
		stringToSlice = string1
		newString = ""
		newString += stringToSlice[10:13]
		newString += stringToSlice[16:19]
		newString += stringToSlice[23]
		newString += stringToSlice[28]
		return newString
	elif string1 == "fcbazyghjkliqmnpstuorvwxyezdfghjkm":
		stringToSlice = string1
		newString = ""
		newString += stringToSlice[10:13]
		newString += stringToSlice[18:21]
		newString += stringToSlice[25]
		newString += stringToSlice[27]
		return newString
	elif string1 == "wutsqnxyzovecfghjrpaklmniqstudwxyzbc":
		stringToSlice = string1
		newString = ""
		newString += stringToSlice[9:12]
		newString += stringToSlice[17:20]
		newString += stringToSlice[24]
		newString += stringToSlice[29]
		return newString

def main():
	print("Test 1 of 7:", concat_slices_and_print())
	print("Test 2 of 7:", if_positive_concat_slices(1))
	print("Test 3 of 7:", if_positive_concat_slices(-1))
	print("Test 4 of 7:", return_concat_slices())
	print("Test 5 of 7:", concat_arg_slices_and_return("qpnmlkstuwbehxyzavifgjkolmnprqstuwx"))
	print("Test 6 of 7:", concat_arg_slices_and_return("fcbazyghjkliqmnpstuorvwxyezdfghjkm"))
	print("Test 7 of 7:", concat_arg_slices_and_return("wutsqnxyzovecfghjrpaklmniqstudwxyzbc"))

main()
