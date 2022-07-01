#
#Ethan Mackenzie Brown
#101031125
#
#Gaddis, T. (2015). "Starting Out With Python"

def func1(int_value):
	if int_value <= 5:
		return [7, 1, 2, 0, 3, 1][int_value]
	elif int_value > 5 and int_value < 13:
		return func1(int_value - 3) + func1(int_value - 4)
	elif int_value >= 13:
		return func1(int_value - 7) - (func1(int_value - 9) % func1(int_value - 7))		
		
def func2(int_value):
	#all if statements check at (-1) because the function is to return n elements, n being int_value in this case
	if int_value - 1 <= 0:
		return [7][:int_value]
	elif int_value - 1 <= 5 and int_value - 1 > 0:
		return func2(int_value - 1) + [func1(int_value - 1)]
	elif int_value - 1 > 5 and int_value - 1 < 13:
		return func2(int_value - 1) + [(func1(int_value - 4) + func1(int_value - 5))]
	elif int_value - 1 >= 13:
		return func2(int_value - 1) + [func1(int_value - 8) - (func1(int_value - 10) % func1(int_value - 8))]
