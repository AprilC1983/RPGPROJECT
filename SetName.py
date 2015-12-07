# Name:		InvestmentCalculator
# Purpose:	Calculates the future value of an investment
# Date:		November 5, 2015
# Author:	April May

from tkinter import *

class SetName:
	def __init__(self):
		window = Tk()
		window.title("Tell us your name")
		
		Label(window, text = "What should we call you? Enter your name below.").grid(row = 1, column = 1, sticky = W)
		
		self.entry = StringVar()
		Entry(window, textvariable = self.entry, justify = RIGHT).grid(row = 2, column = 1)
		
		btOK = Button(window, text = "OK", command = window.destroy).grid(row = 3, column = 1, sticky = E)
		
		window.mainloop()
		
	def getName(self):
		self.__name = self.entry.get()
		return self.__name
