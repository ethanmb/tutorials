#
#Ethan Mackenzie Brown
#101031125
#
#Gaddis, T. (2015). "Starting Out With Python"
from helper import *

for x in range (9):
	goLeft()
	
y = 0
while y < 10:
	goDown()
	y += 1
	
for x in range (1):
	goLeft()
	
counter1 = 0
flag = True
while flag:
	goDown()
	counter1 += 1
	if counter1 == 4:
		flag = False
counter2 = 0		
while True:
	goRight()
	counter2 += 1
	if counter2 == 2:
		break
	