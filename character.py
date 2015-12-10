# Name:		Character
# Purpose:	Class for creating character for game
# Date:		November 20, 2015
# Authors:	Robert Monsen, April May

class Character:#(object):
	def __init__(self, name, type, hp, atk):
		self.name = name
		self.type = type
		self.hp = hp
		self.maxHP = hp
		self.atk = atk
		self.luck = 0
		self.defense = 0
		self.hammer = 0
		
		self.x = 50
		self.y = 175
		self.dx = 2 #move right by default
		self.radius = 5
		self.color = "blue"
		


	def setHP(self, hit):
		self.hp += hit
	def setLuck(self):
		self.luck += 1
	def setDefense(self):
		self.defense += 1
	def setHammer(self):
		self.hammer += 1
	def setAttack(self):
		self.atk += 999
	def heal(self):
		self.hp -= 7
		
	def getNameame(self):
		return self.name
	def getType(self):
		return self.type
	def getHP(self):
		return self.hp
	def getMaxHP(self):
		return self.maxHP
	def getATK(self):
		return self.atk
	def getLuck(self):
		return self.luck
	def getDefense(self):
		return self.defense
	def getHammer(self):
		return self.hammer
