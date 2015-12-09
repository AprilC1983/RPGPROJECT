# Name:		Dragon
# Purpose:	Class for creating dragon
# Date:		November 30, 2015
# Authors:	April May

class Dragon:
	def __init__(self):
		self.hp = 5
		self.atk = 20
		self.x = 350
		self.y = 175
		self.dx = 2 #move right by default
		self.radius = 5
		self.color = "red"
		
	def reduceATK(self):
		self.atk -= 5
	def setHP(self, hit):
		self.hp += hit
	def getATK(self):
		return self.atk
	def getHP(self):
		return self.hp
	
