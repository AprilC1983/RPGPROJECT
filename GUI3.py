# Name:		Game
# Purpose:	Allows user to complete a set of tasks to try and win the game
# Date:		November 20, 2015
# Authors:	Robert Monsen, April May

from tkinter import *

class mainFrame():  #create tkinter GUI class for RPG
	def __init__(self):
		self.window = Tk()
		self.window.title("Enter Kingdom?")
		self.window.geometry("500x340")

        
        
        #add bg image
		background_img = PhotoImage(file='img.gif')
		back = Label(self.window, image=background_img)
		back.place(x=0, y=0, relwidth=1, relheight=1)

        
        
      
        #Displays
		self.text = StringVar()
		self.mainText = Label(self.window, textvariable = self.text,bg="white", wraplength=500,
                              justify=CENTER, width=80, height=14, relief=SUNKEN, borderwidth=3)
		self.text.set("Welcome, traveler! Will you enter our fair kingdom and help us slay the dragon?\nEnter 'Y' or 'N'")
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

           
		self.window.mainloop()

	def processEnter(self, event):
		self.user_text.set(">>> "+self.entryBox.get())
		if(self.entryBox.get()).lower() == 'y':
			self.text.set("That's great news!")
			self.window.title("Welcome!")
		elif(self.entryBox.get()).lower() == 'n':
			self.text.set("Very well. Goodbye.")
			self.window.title("Goodbye")
		elif (self.entryBox.get()).lower() == 'help':
			self.text.set("This is the help. I hope it helps.")
			self.window.title("Help")
		else:
			self.text.set("I'm sorry, I didn't get that.")
		self.entry.set('')
            
	def OnPressEnter(self,event):
		self.processEnter(event)
	def enter(self):
		self.processEnter(None)
    
    
    
mainFrame()
