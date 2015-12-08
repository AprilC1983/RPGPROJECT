# Name:		Game
# Purpose:	Allows user to complete a set of tasks to try and win the game
# Date:		November 20, 2015
# Authors:	Robert Monsen, April May
# Unresolved bugs: cursor focus

from tkinter import *
from random import randint
from Character import Character
from SetName import SetName
from DiamondDefense import DiamondDefense
from Riddle import Riddle
from Dragon import Dragon
from CardChallenge import CardChallenge

class mainFrame:  #create tkinter GUI class for RPG
	def __init__(self, textString):
		self.window = Tk()
		self.window.title("Welcome!")
		self.window.geometry("500x340")

        
        
        #add bg image
		background_img = PhotoImage(file='img.gif')
		back = Label(self.window, image=background_img)
		back.place(x=0, y=0, relwidth=1, relheight=1)

        
        
      
        #Displays
		self.text = StringVar()
		self.mainText = Label(self.window, textvariable = self.text,bg="white", wraplength=500,
                              justify=CENTER, width=80, height=14, relief=SUNKEN, borderwidth=3)
		if textString == "":
			self.text.set("Welcome " + name.getName() + "\nWill you enter our fair kingdom and help us slay the dragon?\nEnter 'Y' or 'N'")
		else:
			self.text.set(textString)
		
		self.mainText.pack()
		self.user_text = StringVar()
		self.userText = Label(self.window, text=">>> ",textvariable = self.user_text,
                              bg="white", width=80, relief=SUNKEN, borderwidth=3)
		self.userText.pack()

        #entrybox
		self.entry = StringVar()
		self.entryBox = Entry(self.window, textvariable = self.entry, width=40)
		self.entryBox.pack()
		self.entryBox.bind("<Return>", self.OnPressEnter)
        #Button
		button = Button(self.window, text = "Enter", command = self.enter)
		button.pack()
		
		self.trial = 99

           
		self.window.mainloop()
	

	def processEnter(self, event):
		self.user_text.set("-- " + self.entryBox.get() + " --")
		if(self.entryBox.get()).lower() == 'y':
			self.text.set("That's great news!\nBefore you face the dragon, you must complete 3 trials.\nBegin a trial by entering its number (1, 2, or 3)\nEnter 'help' for more information.")
			self.window.title("Welcome!")
		elif(self.entryBox.get()).lower() == 'n':
			self.text.set("Fine, who needs you anyway? We'll slay the dragon ourselves!")
			self.window.title("Goodbye")
		elif (self.entryBox.get()).lower() == 'help':
			self.text.set("If you wish to slay the dragon, you must complete 3 trials.\nFor information on a specific trial, enter 'help' plus the number of the trial.\nFor example: 'help 3'")
			self.window.title("Help")
		elif (self.entryBox.get()).lower() == '1':
			self.trial = 1
			self.window.destroy()
		elif (self.entryBox.get()).lower() == '2':
			self.trial = 2	
			self.window.destroy()
		elif (self.entryBox.get()).lower() == '3':
			self.trial = 3
			self.window.destroy()
		elif (self.entryBox.get()).lower() == 'help 1':
			self.text.set("In the first trial, you must find the Diamond of Defense.\nIt's hidden under one of the floor tiles.\nYou will have 3 guesses.")
		elif (self.entryBox.get()).lower() == 'help 2':
			self.text.set("In the second trial you must solve a riddle to attain War Hammer,\nwhich will give you increased strength.\nThink carefully about your answer! You only get one attempt.")
		elif (self.entryBox.get()).lower() == 'help 3':
			self.text.set("The third trial is not a trial at all! It's simply a friendly game of cards.\nThe game is simple. You and your opponent are dealt 5 cards.\nThe numerical value of the cards in your hand is added.\nAces are high. If you have the most points you win!\nWinning gains you Gambler's Luck, which can help you dodge attacks.")
		else:
			self.text.set("I'm sorry, I didn't get that. Try entering it again.")
		self.entry.set('')
            
	def OnPressEnter(self,event):
		self.processEnter(event)
	def enter(self):
		self.processEnter(None)
	
	def getTrial(self):
		return self.trial
		
		
		
class SelectCharacter(object):
	def __init__(self):
		window = Tk()
		window.title("Choose Your Character")
		
		self.__type = "Great Void"
		self.__hp = 999
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
			self.__atk = 15
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
			self.__hp = 9
			self.__atk = 11
		elif self.v1.get() == '5':
			self.__type = "Fairy"
			self.__hp = 7
			self.__atk = 10
		elif self.v1.get() == '6':
			self.__type = "The Void"
			self.__hp = 999
	
	def getType(self):
		return self.__type
	def getHP(self):
		return self.__hp
	def getATK(self):
		return self.__atk


charType = SelectCharacter()
name = SetName()
player = Character(name.getName(), charType.getType(), charType.getHP(), charType.getATK())
dragon = Dragon()
main = mainFrame("")
while dragon.getHP() != 0 and player.getHP() != 0 and main.getTrial() != 99:
	if main.getTrial() == 1:
		string = ""
		diamond = DiamondDefense()
		if diamond.getDiamondStatus() == 0:
			string = "Oh no! You didn't find the Defense Diamond.\nYou can continue to your next trial, but you might want to try again.\nYou may need it later!"
		elif diamond.getDiamondStatus() == 1:
			string = "Congratulations! You found the Defense Diamond!\nYou may choose your next trial.\nIf you have completed all the trials, you are ready to face the dragon!"
		main = mainFrame(string)
	elif main.getTrial() == 2:
		string = ""
		riddle = Riddle()
		if riddle.getHammer() == 0:
			string = "Oh no! You did not attain War Hammer.\nYou can continue to your next trial, but you might want to try again.\nYou may need it later!"
		elif riddle.getHammer() == 1:
			string = "Congratulations! You have attained War Hammer!\nYou may choose your next trial.\nIf you have completed all the trials, you are ready to face the dragon!"
		main = mainFrame(string)
	elif main.getTrial() == 3:
		string = ""
		card = CardChallenge()
		if card.getLuckStatus() == 0:
			string = "Oh no! You did not attain Gambler's Luck.\nYou can continue to your next trial, but you might want to try again.\nYou may need it later!"
		elif card.getLuckStatus() == 1:
			string = "Congratulations! You have attained Gambler's Luck!\nYou may choose your next trial.\nIf you have completed all the trials, you are ready to face the dragon!"
		main = mainFrame(string)
