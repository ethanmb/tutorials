#
#Ethan Mackenzie Brown
#101031125
#
#Gaddis, T. (2015). "Starting Out With Python"

import sys

#function to check if user wants to continue playing, has one integer argument that is intended to start over the quiz when the amount of questions is complete
def quit(x):
	continueUser = input("Would you like to continue to play? (Y for Yes, N for No)")
	if continueUser.lower()=="n":
		#closes program, found this in textbook
		sys.exit()
	elif not(continueUser.lower()=="y"):
		quit(0)
	elif x == 14 and continueUser.lower()=="y":
		play(0)
		
#bulk of quiz in a function, has one integer argument that is inteneded to keep track of the user's score	
def play(userScore):
	questionList = [["What is 2 + 2?", 1, "MC"], ["What is 3 + 3?", 2, "MC"], ["What is 4 + 4?", 3, "MC"], ["What is 5 + 5?", 4, "MC"], ["What is 6 + 6?", 5, "MC"], ["What is 6 - 1?", 6, "MC"], ["What is 5 - 2?", 7, "MC"], ["What is 3 - 3?", 8, "MC"], ["What is 3 * 3?", 9, "MC"], ["What is 6 * 7?", 10, "MC"], ["4 / 2 = 3. True or False?", 11, "TF"], ["6 / 2 = 3. True or False?", 12, "TF"], ["2*(3 / 2) = 3. True or False?", 13, "TF"], ["4^2 = 8. True or False?", 14, "TF"], ["9 + 10 = 21. True or False?", 15, "TF"]]
	answerList = [["2", "3", "4", 2, -1], ["3", "33", "6", 2, -1], ["16", "8", "44", 1, -1], ["10", "55", "4", 0, -1], ["12", "13", "14", 0, -1], ["2", "5", "4", 1, -1], ["2", "3", "4", 1, -1], ["0", "0.3", "4", 0, -1], ["9", "6", "27", 0, -1], ["36", "41", "42", 2, -1], [False, -1], [True, -1], [True, -1], [False, -1], [False, -1]]
	for x in range(15):
		print("Question ", questionList[x][1], ". ",questionList[x][0], sep="")
		#checks to see if question is multiple choice to properly display choices
		if questionList[x][2] == "MC":
		
			for y in range(3):
				if y == 0:
					print("  a.", end="")
				elif y == 1:
					print("  b.", end="")
				else:
					print("  c.", end="")
				print(answerList[x][y])
				
			userInput = input()
			if userInput.lower() == "a" or userInput == answerList[x][0]:
				answerList[x][4] = 0
			elif userInput.lower() == "b" or userInput == answerList[x][1]:
				answerList[x][4] = 1
			elif userInput.lower() == "c" or userInput == answerList[x][2]:
				answerList[x][4] = 2
				
			if answerList[x][4] == answerList[x][3]:
				userScore += 1
		#if the question isn't multiple choice, it is True or false, displays questions and properly takes in answers
		else:
			userInput = input()
			if userInput.lower() == "t" or userInput.lower() == "true":
				answerList[x][1] = True
			elif userInput.lower() == "f" or userInput.lower() == "false":
				answerList[x][1] = False
			if answerList[x][1] == answerList[x][0]:
				userScore += 1
		#calls quit function if it isn't on the final question
		if x < 14:
			quit(x)
		if x == 14:
			print("Congratulations! You have completed the quiz with a score of: ", userScore, " out of 15. Which is ", (userScore/15)*100, "%", sep ="")
			quit(x)
#calls play function with the start of the user's score at 0		
play(0)