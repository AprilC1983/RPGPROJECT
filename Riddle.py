# Name:		Riddle
# Purpose:	Asks the user a riddle
# Date:		November 29, 2015
# Author:	April May
#Bugs:		Fix layout

from tkinter import *

class Riddle:
	def __init__(self):
		trial2 = Tk()
		trial2.title("Riddle me this")
		
		Label(trial2, text = "I am greater than God\nMore evil than the devil\nThe poor have me\n The rich need me\nIf you eat me you will die\nWhat am I?").grid(row = 1, column = 1, sticky = W)
		
		self.riddleAnswer = StringVar()
		Entry(trial2, textvariable = self.riddleAnswer, justify = RIGHT).grid(row = 1, column = 2)
		
		self.result = StringVar()
		lblResult = Label(trial2, textvariable = self.result).grid(row = 4, column = 2, sticky = E)
		
		btCalculate = Button(trial2, text = "Answer the riddle", command = self.calculate).grid(row = 5, column = 2, sticky = E)
		
		trial2.mainloop()
		
	def calculate(self):
		riddleAnswer = self.riddleAnswer.get()
		if riddleAnswer.lower() == 'nothing':
			self.result.set("Correct!")
		else:
			self.result.set("Sorry, that wasn't the right answer.")
Riddle()
