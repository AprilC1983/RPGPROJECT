# Name:		DiamondDefense
# Purpose:	Similar to Battleship, allows user to guess location of Defense Diamond
# Date:		November 27, 2015
# Authors:	April May
# Unresolved bugs: Board not refreshing

from random import randint
from tkinter import *

class DiamondDefense:
	def __init__(self):
	
		self.trial1 = Tk()
		self.trial1.title("Diamond Defense")
			
#		self.board = []
		self.buttons = []
	
#		for x in range(5):
#			self.board.append(["[*]"] * 5)
		
		Label(self.trial1, text = "Pick a floor tile to rip up! You have 3 guesses.").grid(row = 1, column = 1, sticky = W)

		for x in range(5):
			self.buttons.append(Button(self.trial1, text = "  ?  ", command = self.check).grid(row = 1, column = x + 2))
		for x in range(5):
			self.buttons.append(Button(self.trial1, text = "  ?  ", command = self.check).grid(row = 2, column = x + 2))
		for x in range(5):
			self.buttons.append(Button(self.trial1, text = "  ?  ", command = self.check).grid(row = 3, column = x + 2))
		for x in range(5):
			self.buttons.append(Button(self.trial1, text = "  ?  ", command = self.check).grid(row = 4, column = x + 2))
		for x in range(5):
			self.buttons.append(Button(self.trial1, text = "  ?  ", command = self.check).grid(row = 5, column = x + 2))
	
		self.__diamond = 0
	

		def random_row(board):
			return randint(0, len(board) - 1)

		self.diamond_row = random_row(self.buttons)
		print (self.diamond_row)
		self.turn = 0
		
		self.trial1.mainloop()
	
	def getDiamondStatus(self):
		return self.__diamond
	
	def check(self):
		self.__diamond = 1
		self.trial1.destroy()


'''		if self.__row == self.diamond_row and self.__col == self.diamond_col:
			self.__diamond = 1
			self.trial1.destroy()
		else:
			if self.__row < 0 or self.__row > 4 or self.__col < 0 or self.__col > 4:
				self.__result.set("Sorry, you can only search in this room..")
			elif(self.board[self.__row][self.__col] == " X "):
				self.__result.set("You pulled that one up already.")
			else:
				self.__result.set("Nope, it isn't there!!")
				self.board[self.__row][self.__col] = " X "
				self.turn += 1
           
			if self.turn == 3:
				self.trial1.destroy()
				
#		self.__guesses.set(str(self.turn))'''
		
			
#DiamondDefense()
