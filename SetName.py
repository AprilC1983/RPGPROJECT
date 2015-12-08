# Name:		SetName
# Purpose:	Prompts the user for their name
# Date:		November 30, 2015
# Author:	April May

from tkinter import *

class SetName:
	def __init__(self):
		window = Tk()
		window.title("Tell us your name")
		
		Label(window, text = "What should we call you? Enter your name below.").pack()
		
		self.entry = StringVar()
		Entry(window, textvariable = self.entry, justify = RIGHT).pack()
		
		btOK = Button(window, text = "OK", command = window.destroy).pack()
		
		window.mainloop()
		
	def getName(self):
		self.__name = self.entry.get()
		return self.__name
