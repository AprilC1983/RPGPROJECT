# Name:		CardChallenge
# Purpose:	Allows user to play a card game
# Date:		December 3, 2015
# Authors:	April May
# Unresolved bugs: 

from tkinter import *
import random

class CardChallenge:
	def __init__(self):
		self.window = Tk() 
		self.window.title("Card Challenge")
		
		self.opponentScore = 0
		self.myScore = 0
		self.luck = 0
			
		frame1 = Frame(self.window)
		frame1.pack()
		
		cardBack = PhotoImage(file = "cards/b2fv.png")
		
		self.labelList1 = []
		for i in range(5):
			self.labelList1.append(Label(frame1, image = cardBack))
			self.labelList1[i].pack(side = LEFT)
			
		self.button1 = Button(self.window, text="Reveal Opponent's Cards", state=NORMAL, command=self.revealOpponent)
		self.button1.pack()
		
		frame2 = Frame(self.window)
		frame2.pack()
		
		cardBack2 = PhotoImage(file = "cards/backCard.png")
		
		self.labelList2 = []
		for i in range(5):
			self.labelList2.append(Label(frame2, image = cardBack2))
			self.labelList2[i].pack(side = LEFT)
		
		
		self.button2 = Button(self.window, text="Reveal Your Cards", state=NORMAL, command=self.revealYourCards)
		self.button2.pack()
		
		self.gameOutcome = StringVar()
		self.lblOutcome = Label(self.window, textvariable = self.gameOutcome)
		self.lblOutcome.pack()
		
		self.closeButton = Button(self.window, text="Exit", state=NORMAL, command=self.window.destroy)
		self.closeButton.pack()
		
		self.deck = []
		
		self.cardImages = []
		for i in range(1, 53):
			self.cardImages.append(PhotoImage(file = "cards/" + str(i) + ".png"))
		
		
		self.window.mainloop()
		
	def define_cards(self, n):
		self.rank_string = ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"]
		self.suit_string = ["clubs", "diamonds", "hearts", "spades"]
		self.cards = []

		for suit in range(len(self.suit_string)):
			for rank in range(len(self.rank_string)):
				self.card_string = self.rank_string[rank] + " of " + self.suit_string[suit]
				self.cards.append(self.card_string)

		for x in range(len(self.cards)):
			return self.cards[n]
		
	def create_deck(self, deck):
		for i in range(52):
			self.deck.append(i)
		return
	
	def shuffle_deck(self, deck):
		random.shuffle(self.deck)
		return
	
	def deal_cards(self, deck):
		return self.deck.pop(0)
	
	def getLuckStatus(self):
		return self.luck
		
		#Reveal opponent's hand
	def revealOpponent(self):
		self.create_deck(self.deck)
		self.shuffle_deck(self.deck)
		for i in range(5):
			card = self.deal_cards(self.deck)
			if self.define_cards(card) == "ace of spades":
				self.labelList1[i]["image"] = self.cardImages[0]
				self.opponentScore += 14
			elif self.define_cards(card) == "two of spades":
				self.labelList1[i]["image"] = self.cardImages[1]
				self.opponentScore += 2
			elif self.define_cards(card) == "three of spades":
				self.labelList1[i]["image"] = self.cardImages[2]
				self.opponentScore += 3
			elif self.define_cards(card) == "four of spades":
				self.labelList1[i]["image"] = self.cardImages[3]
				self.opponentScore += 4
			elif self.define_cards(card) == "five of spades":
				self.labelList1[i]["image"] = self.cardImages[4]
				self.opponentScore += 5
			elif self.define_cards(card) == "six of spades":
				self.labelList1[i]["image"] = self.cardImages[5]
				self.opponentScore += 6
			elif self.define_cards(card) == "seven of spades":
				self.labelList1[i]["image"] = self.cardImages[6]
				self.opponentScore += 7
			elif self.define_cards(card) == "eight of spades":
				self.labelList1[i]["image"] = self.cardImages[7]
				self.opponentScore += 8
			elif self.define_cards(card) == "nine of spades":
				self.labelList1[i]["image"] = self.cardImages[8]
				self.opponentScore += 9
			elif self.define_cards(card) == "ten of spades":
				self.labelList1[i]["image"] = self.cardImages[9]
				self.opponentScore += 10
			elif self.define_cards(card) == "jack of spades":
				self.labelList1[i]["image"] = self.cardImages[10]
				self.opponentScore += 11
			elif self.define_cards(card) == "queen of spades":
				self.labelList1[i]["image"] = self.cardImages[11]
				self.opponentScore += 12
			elif self.define_cards(card) == "king of spades":
				self.labelList1[i]["image"] = self.cardImages[12]
				self.opponentScore += 13
			elif self.define_cards(card) == "ace of hearts":
				self.labelList1[i]["image"] = self.cardImages[13]
				self.opponentScore += 14
			elif self.define_cards(card) == "two of hearts":
				self.labelList1[i]["image"] = self.cardImages[14]
				self.opponentScore += 2
			elif self.define_cards(card) == "three of hearts":
				self.labelList1[i]["image"] = self.cardImages[15]
				self.opponentScore += 3
			elif self.define_cards(card) == "four of hearts":
				self.labelList1[i]["image"] = self.cardImages[16]
				self.opponentScore += 4
			elif self.define_cards(card) == "five of hearts":
				self.labelList1[i]["image"] = self.cardImages[17]
				self.opponentScore += 5
			elif self.define_cards(card) == "six of hearts":
				self.labelList1[i]["image"] = self.cardImages[18]
				self.opponentScore += 6
			elif self.define_cards(card) == "seven of hearts":
				self.labelList1[i]["image"] = self.cardImages[19]
				self.opponentScore += 7
			elif self.define_cards(card) == "eight of hearts":
				self.labelList1[i]["image"] = self.cardImages[20]
				self.opponentScore += 8
			elif self.define_cards(card) == "nine of hearts":
				self.labelList1[i]["image"] = self.cardImages[21]
				self.opponentScore += 9
			elif self.define_cards(card) == "ten of hearts":
				self.labelList1[i]["image"] = self.cardImages[22]
				self.opponentScore += 10
			elif self.define_cards(card) == "jack of hearts":
				self.labelList1[i]["image"] = self.cardImages[23]
				self.opponentScore += 11
			elif self.define_cards(card) == "queen of hearts":
				self.labelList1[i]["image"] = self.cardImages[24]
				self.opponentScore += 12
			elif self.define_cards(card) == "king of hearts":
				self.labelList1[i]["image"] = self.cardImages[25]
				self.opponentScore += 13
			elif self.define_cards(card) == "ace of diamonds":
				self.labelList1[i]["image"] = self.cardImages[26]
				self.opponentScore += 14
			elif self.define_cards(card) == "two of diamonds":
				self.labelList1[i]["image"] = self.cardImages[27]
				self.opponentScore += 2
			elif self.define_cards(card) == "three of diamonds":
				self.labelList1[i]["image"] = self.cardImages[28]
				self.opponentScore += 3
			elif self.define_cards(card) == "four of diamonds":
				self.labelList1[i]["image"] = self.cardImages[29]
				self.opponentScore += 4
			elif self.define_cards(card) == "five of diamonds":
				self.labelList1[i]["image"] = self.cardImages[30]
				self.opponentScore += 5
			elif self.define_cards(card) == "six of diamonds":
				self.labelList1[i]["image"] = self.cardImages[31]
				self.opponentScore += 6
			elif self.define_cards(card) == "seven of diamonds":
				self.labelList1[i]["image"] = self.cardImages[32]
				self.opponentScore += 7
			elif self.define_cards(card) == "eight of diamonds":
				self.labelList1[i]["image"] = self.cardImages[33]
				self.opponentScore += 8
			elif self.define_cards(card) == "nine of diamonds":
				self.labelList1[i]["image"] = self.cardImages[34]
				self.opponentScore += 9
			elif self.define_cards(card) == "ten of diamonds":
				self.labelList1[i]["image"] = self.cardImages[35]
				self.opponentScore += 10
			elif self.define_cards(card) == "jack of diamonds":
				self.labelList1[i]["image"] = self.cardImages[36]
				self.opponentScore += 11
			elif self.define_cards(card) == "queen of diamonds":
				self.labelList1[i]["image"] = self.cardImages[37]
				self.opponentScore += 12
			elif self.define_cards(card) == "king of diamonds":
				self.labelList1[i]["image"] = self.cardImages[38]
				self.opponentScore += 13
			elif self.define_cards(card) == "ace of clubs":
				self.labelList1[i]["image"] = self.cardImages[39]
				self.opponentScore += 14
			elif self.define_cards(card) == "two of clubs":
				self.labelList1[i]["image"] = self.cardImages[40]
				self.opponentScore += 2
			elif self.define_cards(card) == "three of clubs":
				self.labelList1[i]["image"] = self.cardImages[41]
				self.opponentScore += 3
			elif self.define_cards(card) == "four of clubs":
				self.labelList1[i]["image"] = self.cardImages[42]
				self.opponentScore += 4
			elif self.define_cards(card) == "five of clubs":
				self.labelList1[i]["image"] = self.cardImages[43]
				self.opponentScore += 5
			elif self.define_cards(card) == "six of clubs":
				self.labelList1[i]["image"] = self.cardImages[44]
				self.opponentScore += 6
			elif self.define_cards(card) == "seven of clubs":
				self.labelList1[i]["image"] = self.cardImages[45]
				self.opponentScore += 7
			elif self.define_cards(card) == "eight of clubs":
				self.labelList1[i]["image"] = self.cardImages[46]
				self.opponentScore += 8
			elif self.define_cards(card) == "nine of clubs":
				self.labelList1[i]["image"] = self.cardImages[47]
				self.opponentScore += 9
			elif self.define_cards(card) == "ten of clubs":
				self.labelList1[i]["image"] = self.cardImages[48]
				self.opponentScore += 10
			elif self.define_cards(card) == "jack of clubs":
				self.labelList1[i]["image"] = self.cardImages[49]
				self.opponentScore += 11
			elif self.define_cards(card) == "queen of clubs":
				self.labelList1[i]["image"] = self.cardImages[50]
				self.opponentScore += 12
			elif self.define_cards(card) == "king of clubs":
				self.labelList1[i]["image"] = self.cardImages[51]
				self.opponentScore += 13
				
		if self.button2["state"] == "disabled":
			if self.myScore > self.opponentScore:
				self.gameOutcome.set("You won!")
				self.luck = 1
			elif self.myScore < self.opponentScore:
				self.gameOutcome.set("Too bad. Maybe next time.")		
		
		self.button1.config(state = "disabled")
		
		#Reveal your hand
	def revealYourCards(self):
		self.create_deck(self.deck)
		self.shuffle_deck(self.deck)
		for i in range(5):
			card = self.deal_cards(self.deck)
			if self.define_cards(card) == "ace of spades":
				self.labelList2[i]["image"] = self.cardImages[0]
				self.myScore += 14
			elif self.define_cards(card) == "two of spades":
				self.labelList2[i]["image"] = self.cardImages[1]
				self.myScore += 2
			elif self.define_cards(card) == "three of spades":
				self.labelList2[i]["image"] = self.cardImages[2]
				self.myScore += 3
			elif self.define_cards(card) == "four of spades":
				self.labelList2[i]["image"] = self.cardImages[3]
				self.myScore += 4
			elif self.define_cards(card) == "five of spades":
				self.labelList2[i]["image"] = self.cardImages[4]
				self.myScore += 5
			elif self.define_cards(card) == "six of spades":
				self.labelList2[i]["image"] = self.cardImages[5]
				self.myScore += 6
			elif self.define_cards(card) == "seven of spades":
				self.labelList2[i]["image"] = self.cardImages[6]
				self.myScore += 7
			elif self.define_cards(card) == "eight of spades":
				self.labelList2[i]["image"] = self.cardImages[7]
				self.myScore += 8
			elif self.define_cards(card) == "nine of spades":
				self.labelList2[i]["image"] = self.cardImages[8]
				self.myScore += 9
			elif self.define_cards(card) == "ten of spades":
				self.labelList2[i]["image"] = self.cardImages[9]
				self.myScore += 10
			elif self.define_cards(card) == "jack of spades":
				self.labelList2[i]["image"] = self.cardImages[10]
				self.myScore += 11
			elif self.define_cards(card) == "queen of spades":
				self.labelList2[i]["image"] = self.cardImages[11]
				self.myScore += 12
			elif self.define_cards(card) == "king of spades":
				self.labelList2[i]["image"] = self.cardImages[12]
				self.myScore += 13
			elif self.define_cards(card) == "ace of hearts":
				self.labelList2[i]["image"] = self.cardImages[13]
				self.myScore += 14
			elif self.define_cards(card) == "two of hearts":
				self.labelList2[i]["image"] = self.cardImages[14]
				self.myScore += 2
			elif self.define_cards(card) == "three of hearts":
				self.labelList2[i]["image"] = self.cardImages[15]
				self.myScore += 3
			elif self.define_cards(card) == "four of hearts":
				self.labelList2[i]["image"] = self.cardImages[16]
				self.myScore += 4
			elif self.define_cards(card) == "five of hearts":
				self.labelList2[i]["image"] = self.cardImages[17]
				self.myScore += 5
			elif self.define_cards(card) == "six of hearts":
				self.labelList2[i]["image"] = self.cardImages[18]
				self.myScore += 6
			elif self.define_cards(card) == "seven of hearts":
				self.labelList2[i]["image"] = self.cardImages[19]
				self.myScore += 7
			elif self.define_cards(card) == "eight of hearts":
				self.labelList2[i]["image"] = self.cardImages[20]
				self.myScore += 8
			elif self.define_cards(card) == "nine of hearts":
				self.labelList2[i]["image"] = self.cardImages[21]
				self.myScore += 9
			elif self.define_cards(card) == "ten of hearts":
				self.labelList2[i]["image"] = self.cardImages[22]
				self.myScore += 10
			elif self.define_cards(card) == "jack of hearts":
				self.labelList2[i]["image"] = self.cardImages[23]
				self.myScore += 11
			elif self.define_cards(card) == "queen of hearts":
				self.labelList2[i]["image"] = self.cardImages[24]
				self.myScore += 12
			elif self.define_cards(card) == "king of hearts":
				self.labelList2[i]["image"] = self.cardImages[25]
				self.myScore += 13
			elif self.define_cards(card) == "ace of diamonds":
				self.labelList2[i]["image"] = self.cardImages[26]
				self.myScore += 14
			elif self.define_cards(card) == "two of diamonds":
				self.labelList2[i]["image"] = self.cardImages[27]
				self.myScore += 2
			elif self.define_cards(card) == "three of diamonds":
				self.labelList2[i]["image"] = self.cardImages[28]
				self.myScore += 3
			elif self.define_cards(card) == "four of diamonds":
				self.labelList2[i]["image"] = self.cardImages[29]
				self.myScore += 4
			elif self.define_cards(card) == "five of diamonds":
				self.labelList2[i]["image"] = self.cardImages[30]
				self.myScore += 5
			elif self.define_cards(card) == "six of diamonds":
				self.labelList2[i]["image"] = self.cardImages[31]
				self.myScore += 6
			elif self.define_cards(card) == "seven of diamonds":
				self.labelList2[i]["image"] = self.cardImages[32]
				self.myScore += 7
			elif self.define_cards(card) == "eight of diamonds":
				self.labelList2[i]["image"] = self.cardImages[33]
				self.myScore += 8
			elif self.define_cards(card) == "nine of diamonds":
				self.labelList2[i]["image"] = self.cardImages[34]
				self.myScore += 9
			elif self.define_cards(card) == "ten of diamonds":
				self.labelList2[i]["image"] = self.cardImages[35]
				self.myScore += 10
			elif self.define_cards(card) == "jack of diamonds":
				self.labelList2[i]["image"] = self.cardImages[36]
				self.myScore += 11
			elif self.define_cards(card) == "queen of diamonds":
				self.labelList2[i]["image"] = self.cardImages[37]
				self.myScore += 12
			elif self.define_cards(card) == "king of diamonds":
				self.labelList2[i]["image"] = self.cardImages[38]
				self.myScore += 13
			elif self.define_cards(card) == "ace of clubs":
				self.labelList2[i]["image"] = self.cardImages[39]
				self.myScore += 14
			elif self.define_cards(card) == "two of clubs":
				self.labelList2[i]["image"] = self.cardImages[40]
				self.myScore += 2
			elif self.define_cards(card) == "three of clubs":
				self.labelList2[i]["image"] = self.cardImages[41]
				self.myScore += 3
			elif self.define_cards(card) == "four of clubs":
				self.labelList2[i]["image"] = self.cardImages[42]
				self.myScore += 4
			elif self.define_cards(card) == "five of clubs":
				self.labelList2[i]["image"] = self.cardImages[43]
				self.myScore += 5
			elif self.define_cards(card) == "six of clubs":
				self.labelList2[i]["image"] = self.cardImages[44]
				self.myScore += 6
			elif self.define_cards(card) == "seven of clubs":
				self.labelList2[i]["image"] = self.cardImages[45]
				self.myScore += 7
			elif self.define_cards(card) == "eight of clubs":
				self.labelList2[i]["image"] = self.cardImages[46]
				self.myScore += 8
			elif self.define_cards(card) == "nine of clubs":
				self.labelList2[i]["image"] = self.cardImages[47]
				self.myScore += 9
			elif self.define_cards(card) == "ten of clubs":
				self.labelList2[i]["image"] = self.cardImages[48]
				self.myScore += 10
			elif self.define_cards(card) == "jack of clubs":
				self.labelList2[i]["image"] = self.cardImages[49]
				self.myScore += 11
			elif self.define_cards(card) == "queen of clubs":
				self.labelList2[i]["image"] = self.cardImages[50]
				self.myScore += 12
			elif self.define_cards(card) == "king of clubs":
				self.labelList2[i]["image"] = self.cardImages[51]
				self.myScore += 13
		if self.button1["state"] == "disabled":
			if self.myScore > self.opponentScore:
				self.gameOutcome.set("You won!")
				self.luck = 1
			elif self.myScore < self.opponentScore:
				self.gameOutcome.set("Too bad. Maybe next time.")
		self.button2.config(state = "disabled")		
#CardChallenge()
