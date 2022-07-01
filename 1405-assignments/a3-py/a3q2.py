#
#Ethan Mackenzie Brown
#101031125
#
#Gaddis, T. (2015). "Starting Out With Python"
#2. Built-in Functions. (2016-10-14). Retrieved from https://docs.python.org/3/library/functions.html


#number between 0 and 9 that is divisible by 3								
for x in range(0, 10, 3):
	#letter between E and G including E and excluding G (unicode for capital E is 69, and F is 70 in decimal)
	for y in range (69, 71, 1):
		#letter between J and K excluding J and including K (unicode for capital K is 75 in decimal)
		for z in range (75, 76, 1):
			#number between 4 and 5 excluding 4 and including 5
			for xx in range (5, 6, 1):
				#number between 0 and 5 including 0 and excluding 5
				for xy in range(5):
					#number between 1 and 9 that is divisible by 2
					for xz in range(2, 9, 2):
						print(x, chr(y), chr(z), xx, xy, xz, sep="")
						print()