# Name:		DiamondDefense
# Purpose:	Similar to Battleship, allows user to guess location of Defense Diamond
# Date:		November 27, 2015
# Authors:	April May
# Unresolved bugs: Board not refreshing

from random import randint
from tkinter import *

class DiamondDefense:
	def __init__(self):
	
		self.window = Tk()
		self.window.title("Diamond Defense")
			
		self.board = []
	
		for x in range(5):
			self.board.append(["[*]"] * 5)
		
		Label(self.window, text = "Pick a floor tile to rip up!").grid(row = 1, column = 2, sticky = W)
		Label(self.window, text = "Row: ").grid(row = 2, column = 1, sticky = W)
		Label(self.window, text = "Column: ").grid(row = 3, column = 1, sticky = W)
		Label(self.window, text = "Guesses Taken: ").grid(row = 10, column = 1, sticky = W)
		self.__row1 = Label(self.window, text = " ".join(self.board[0])).grid(row = 5, column = 1, sticky = W)
		self.__row2 = Label(self.window, text = " ".join(self.board[1])).grid(row = 6, column = 1, sticky = W)
		self.__row3 = Label(self.window, text = " ".join(self.board[2])).grid(row = 7, column = 1, sticky = W)
		self.__row4 = Label(self.window, text = " ".join(self.board[3])).grid(row = 8, column = 1, sticky = W)
		self.__row5 = Label(self.window, text = " ".join(self.board[4])).grid(row = 9, column = 1, sticky = W)
		
		self.__result = StringVar()
		Entry(self.window, textvariable = self.__result, justify = RIGHT).grid(row = 9, column = 2)
		self.__guess_row = StringVar()
		Entry(self.window, textvariable = self.__guess_row, justify = RIGHT).grid(row = 2, column = 2)
		self.__guess_col = StringVar()
		Entry(self.window, textvariable = self.__guess_col, justify = RIGHT).grid(row = 3, column = 2)
		self.__guesses = StringVar()
		Entry(self.window, textvariable = self.__guesses, justify = RIGHT).grid(row = 10, column = 2)
		
		btCheck = Button(self.window, text = "Rip it up!", command = self.check).grid(row = 4, column = 2, sticky = E)
	
		self.__diamond = 0
	

		def random_row(board):
			return randint(0, len(board) - 1)

		def random_col(board):
			return randint(0, len(board[0]) - 1)

		self.diamond_row = random_row(self.board)
		self.diamond_col = random_col(self.board)
		print (self.diamond_row)
		print (self.diamond_col)
		self.turn = 0
		
		self.window.mainloop()
		
	def check(self):

		self.__row = int(self.__guess_row.get()) - 1
		self.__col = int(self.__guess_col.get()) - 1

		if self.__row == self.diamond_row and self.__col == self.diamond_col:
			self.__diamond = 1
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
				self.window.destroy()
				
		self.__guesses.set(str(self.turn))
		self.__guess_row.set('')
		self.__guess_col.set('')
		
	def getDiamondStatus(self):
		return self.__diamond
			
