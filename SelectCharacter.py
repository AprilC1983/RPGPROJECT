# Name:		SelectCharacter
# Purpose:	Allows user to chooose what type of character to play
# Date:		November 25, 2015
# Authors:	Robert Monsen, April May
		
class SelectCharacter():
	def __init__(self):
		window = Tk()
		window.title("Choose Your Character")
		
		type = ""
		frame1 = Frame(window)
		frame1.pack()
		self.v1 = StringVar()
		rbWizard = Radiobutton(frame1, text = "Wizard", variable = self.v1, value = '1', command = self.processRadiobutton)
		rbElf = Radiobutton(frame1, text = "Elf", variable = self.v1, value = '2', command = self.processRadiobutton)
		rbKnight = Radiobutton(frame1, text = "Knight", variable = self.v1, value = '3', command = self.processRadiobutton)
		rbDwarf = Radiobutton(frame1, text = "Dwarf", variable = self.v1, value = '4', command = self.processRadiobutton)
		rbFairy = Radiobutton(frame1, text = "Fairy", variable = self.v1, value = '5', command = self.processRadiobutton)
		
		frame2 = Frame(window)
		frame2.pack()
		self.v2 = 3
		
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
				self.type = "Wizard"
			elif self.v1.get() == '2':
				self.type = "Elf"
			elif self.v1.get() == '3':
				self.type = "Knight"
			elif self.v1.get() == '4':
				self.type = "Dwarf"
			elif self.v1.get() == '5':
				self.type = "Fairy"
	
		def getType(self):
			return self.type
