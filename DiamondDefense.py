# Name:		DiamondDefense
# Purpose:	Similar to Battleship, allows user to guess location of Defense Diamond
# Date:		November 27, 2015
# Authors:	April May
#Bugs:		Note to self, remove print statement when finished with testing


from random import randint
from tkinter import *

class DiamondDefense:
	def __init__(self):
	
		window = Tk()
		window.title("Diamond Defense")
			
		self.buttons = []
	
		
		Label(window, text = "Pick a floor tile to rip up!\nYou have 3 guesses.").pack()
		
		frame = Frame(window)
		frame.pack()
		
		tile = PhotoImage(file = "tile.png")
		self.diamond = PhotoImage(file = "diamond2.png")
		
		button1 = Button(frame, image = tile, command = self.check)
		self.buttons.append(button1)
		button2 = Button(frame, image = tile, command = self.check)
		self.buttons.append(button2)
		button3 = Button(frame, image = tile, command = self.check)
		self.buttons.append(button3)
		button4 = Button(frame, image = tile, command = self.check)
		self.buttons.append(button4)
		button5 = Button(frame, image = tile, command = self.check)
		self.buttons.append(button5)
		button6 = Button(frame, image = tile, command = self.check)
		self.buttons.append(button6)
		button7 = Button(frame, image = tile, command = self.check)
		self.buttons.append(button7)
		button8 = Button(frame, image = tile, command = self.check)
		self.buttons.append(button8)
		button9 = Button(frame, image = tile, command = self.check)
		self.buttons.append(button9)
		button10 = Button(frame, image = tile, command = self.check)
		self.buttons.append(button10)
		button11 = Button(frame, image = tile, command = self.check)
		self.buttons.append(button11)
		button12 = Button(frame, image = tile, command = self.check)
		self.buttons.append(button12)
		button13 = Button(frame, image = tile, command = self.check)
		self.buttons.append(button13)
		button14 = Button(frame, image = tile, command = self.check)
		self.buttons.append(button14)
		button15 = Button(frame, image = tile, command = self.check)
		self.buttons.append(button15)
		button16 = Button(frame, image = tile, command = self.check)
		self.buttons.append(button16)
		button17 = Button(frame, image = tile, command = self.check)
		self.buttons.append(button17)
		button18 = Button(frame, image = tile, command = self.check)
		self.buttons.append(button18)
		button19 = Button(frame, image = tile, command = self.check)
		self.buttons.append(button19)
		button20 = Button(frame, image = tile, command = self.check)
		self.buttons.append(button20)
		button21 = Button(frame, image = tile, command = self.check)
		self.buttons.append(button21)
		button22 = Button(frame, image = tile, command = self.check)
		self.buttons.append(button22)
		button23 = Button(frame, image = tile, command = self.check)
		self.buttons.append(button23)
		button24 = Button(frame, image = tile, command = self.check)
		self.buttons.append(button24)
		button25 = Button(frame, image = tile, command = self.check)
		self.buttons.append(button25)
		for x in range(5):
			self.buttons[x].grid(row = 1, column = x + 2)
		for x in range(5, 10):
			self.buttons[x].grid(row = 2, column = (x - 3))
		for x in range(10, 15):
			self.buttons[x].grid(row = 3, column = (x - 8))
		for x in range(15, 20):
			self.buttons[x].grid(row = 4, column = (x - 13))
		for x in range(20, 25):
			self.buttons[x].grid(row = 5, column = (x - 18))
			
		frame2 = Frame(window)
		frame2.pack()
		
		self.__guesses = StringVar()
		Label(frame2, textvariable = self.__guesses).pack()
		
		self.__outcome = StringVar()
		Label(frame2, textvariable = self.__outcome).pack()
		
		Button(window, text = "Exit", command = window.destroy).pack()
	
		self.__diamond = 0
		
		self.diamond_tile = self.random_row(self.buttons)
		print (self.diamond_tile)
		self.buttons[self.diamond_tile].config(command = self.victory)
		self.turn = 0
		
		window.mainloop()
	

	def random_row(self, board):
		return randint(0, len(board) - 1)

	
	def getDiamondStatus(self):
		return self.__diamond
	
	def check(self):
		pass
		self.turn += 1
		self.__guesses.set("Guesses Taken: " + str(self.turn))
		if self.turn >= 3:
			self.__outcome.set("Aw, rats! Maybe next time.")
			for x in self.buttons:
				x.config(state = "disabled")
	
	def blank(self):
		pass
		
	def victory(self):
		self.__diamond += 1
		self.turn += 1
		self.__guesses.set("Guesses Taken: " + str(self.turn))
		self.buttons[self.diamond_tile].config(image = self.diamond)
		self.__outcome.set("Victory! You found it!")
		for x in self.buttons:
				x.config(state = "disabled")
		self.buttons[self.diamond_tile].config(state = "normal")
		self.buttons[self.diamond_tile].config(command = self.blank)
		
	
#DiamondDefense()
