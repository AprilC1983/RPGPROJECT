# Name:		Riddle
# Purpose:	Asks the user a riddle
# Date:		November 29, 2015
# Author:	April May
# Bugs:		

from tkinter import *

class Riddle:
	def __init__(self):
		self.trial2 = Tk()
		self.trial2.title("Riddle me this")
		
		self.hammer = 0
		
		Label(self.trial2, text = "I am greater than God\nMore evil than the devil\nThe poor have me\n The rich need me\nIf you eat me you will die\nWhat am I?").pack()
		
		self.riddleAnswer = StringVar()
		Entry(self.trial2, textvariable = self.riddleAnswer, justify = RIGHT).pack()
		
#		self.result = StringVar()
#		lblResult = Label(self.trial2, textvariable = self.result).pack()
		
		btnAnswer = Button(self.trial2, text = "Answer the riddle", command = self.answerRiddle).pack()
		
		self.trial2.mainloop()
		
	def answerRiddle(self):
		riddleAnswer = self.riddleAnswer.get()
		if riddleAnswer.lower() == 'nothing':
#			self.result.set("Correct!")
			self.hammer = 1
			self.trial2.destroy()
		else:
#			self.result.set("Sorry, that wasn't the right answer.")
			self.trial2.destroy()
	def getHammer(self):
		return self.hammer
#Riddle()
