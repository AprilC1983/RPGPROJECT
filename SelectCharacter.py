# Name:		SelectCharacter
# Purpose:	Allows user to chooose what type of character to play
# Date:		November 25, 2015
# Authors:	April May

from tkinter import *
		
class SelectCharacter(object):
	def __init__(self):
		window = Tk()
		window.title("Choose Your Character")
		
		self.__type = "Great Void"
		self.__hp = 5
		self.__atk = 999
		frame1 = Frame(window)
		frame1.pack()
		self.v1 = StringVar()
		rbWizard = Radiobutton(frame1, text = "Wizard", variable = self.v1, value = '1', command = self.processRadiobutton)
		rbElf = Radiobutton(frame1, text = "Elf", variable = self.v1, value = '2', command = self.processRadiobutton)
		rbKnight = Radiobutton(frame1, text = "Knight", variable = self.v1, value = '3', command = self.processRadiobutton)
		rbDwarf = Radiobutton(frame1, text = "Dwarf", variable = self.v1, value = '4', command = self.processRadiobutton)
		rbFairy = Radiobutton(frame1, text = "Fairy", variable = self.v1, value = '5', command = self.processRadiobutton)
		rbTheVoid = Radiobutton(frame1, text = "Nothing", variable = self.v1, value = '6', command = self.processRadiobutton)
		self.v1.set('6')
		
		frame2 = Frame(window)
		frame2.pack()
		self.v2 = 3
		self.lbl = Label(frame2, text = "Choose you character type. When you have made your selection click the 'OK' button.")
		self.lbl.grid(row = 1, column = self.v2)
		
		frame3 = Frame(window)
		frame3.pack()
		
		btnOk = Button(frame3, text = "OK", command = window.destroy)
		
		rbWizard.grid(row = 1, column = 1)
		rbElf.grid(row = 1, column = 2)
		rbKnight.grid(row = 1, column = 3)
		rbDwarf.grid(row = 1, column = 4)
		rbFairy.grid(row = 1, column = 5)
		btnOk.grid(row = 1, column = 3)
		
		window.mainloop()
		
	def processRadiobutton(self):
		if self.v1.get() == '1':
			self.__type = "Wizard"
			self.__hp = 10
			self.__atk = 8
		elif self.v1.get() == '2':
			self.__type = "Elf"
			self.__hp = 8
			self.__atk = 12
		elif self.v1.get() == '3':
			self.__type = "Knight"
			self.__hp = 9
			self.__atk = 12
		elif self.v1.get() == '4':
			self.__type = "Dwarf"
			self.__hp = 15
			self.__atk = 11
		elif self.v1.get() == '5':
			self.__type = "Fairy"
			self.__hp = 20
			self.__atk = 3
		elif self.v1.get() == '6':
			self.__type = "The Void"
			self.__hp = 0
	
	def getType(self):
		return self.__type
	def getHP(self):
		return self.__hp
	def getATK(self):
		return self.__atk
