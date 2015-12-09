# Name:		Arena
# Purpose:	Allows user to battle dragon
# Date:		Dec 5, 2015
# Authors:	April May
# Bugs:		Crashes if exited with corner x instead of self.btnExit

from tkinter import *
from random import randint
from Dragon import Dragon
from Character import Character

		
class Arena:
	def __init__(self, player, dragon):
	
		self.player = player
		self.dragon = dragon
		self.winner = 0
		
		window = Tk()
		window.title("Slay the Dragon!")
		
		self.width = 400
		self.height = 200
		self.canvas = Canvas(window, bg = "white", width = self.width, height = self.height)
		self.canvas.pack()
		
		self.canvas.create_rectangle(25, 200, 35, self.player.getHP(), fill = "green", tags = "playerHP")
		self.canvas.create_rectangle(365, 200, 375, self.dragon.getHP(), fill = "red", tags = "dragonHP")
		
		self.frame1 = Frame(window)
		self.frame1.pack()
		
		self.lblPlayerHP = Label(self.frame1, text = "HP\t\t\t\t")
		self.lblPlayerHP.grid(row = 1, column = 1)
		
		lblDragonHP = Label(self.frame1, text = "\t\t\t\tHP")
		lblDragonHP.grid(row = 1, column = 2)
	
		frame2 = Frame(window)
		frame2.pack()
		
		self.btnAttack = Button(frame2, text = "Attack!", command = self.attack)
		self.btnAttack.pack(side = LEFT)
		
		self.btnWarHammer = Button(frame2, text = "War Hammer", state = DISABLED, command = self.warHammer)
		self.btnWarHammer.pack(side = LEFT)
		if player.getHammer() != 0:
			self.btnWarHammer.config(state = "normal")
		
		self.btnDefense = Button(frame2, text = "Diamond Defense", state = DISABLED, command = self.defend)
		self.btnDefense.pack(side = LEFT)
		if player.getDefense() != 0:
			self.btnDefense.config(state = "normal")
		
		self.btnLuck = Button(frame2, text = "Gambler's Luck", state = DISABLED, command = self.chance)
		self.btnLuck.pack(side = LEFT)
		if player.getLuck() != 0:
			self.btnLuck.config(state = "normal")
		
		frame3 = Frame(window)
		frame3.pack()
		
		self.btnExit = Button(frame3, text = "Exit", state = DISABLED, command = window.destroy)
		self.btnExit.pack()
		
		
		self.sleepTime = 15
		self.isStopped = False
		self.animate()
		
		window.mainloop()
		
	def attack(self):
		num = randint(1, 2)
		if num == 1:
			self.player.setHP(self.dragon.getATK())
			self.canvas.delete("playerHP")
			self.canvas.create_rectangle(25, 200, 35, self.player.getHP(), fill = "green", tags = "playerHP")
			if self.player.getHP() >= 200:
				self.winner = 2
				self.btnAttack.config(state = "disabled")
				self.canvas.create_text(200, 30, text = "YOU DIED", tags = "text", fill = "red")
				self.isStopped = True
				self.btnExit.config(state = "normal")
		self.dragon.setHP(self.player.getATK())
		self.canvas.delete("dragonHP")
		self.canvas.create_rectangle(365, 200, 375, self.dragon.getHP(), fill = "red", tags = "dragonHP")
		if self.dragon.getHP() >= 200:
			self.winner = 1
			self.btnAttack.config(state = "disabled")
			self.canvas.create_text(200, 30, text = "WINNER!", tags = "text", fill = "green")
			self.isStopped = True
			self.btnExit.config(state = "normal")
		
		
	def warHammer(self):
		self.player.setAttack()
		self.btnWarHammer.config(state = "disabled")
		
	def defend(self):
		self.dragon.reduceATK()
		self.btnDefense.config(state = "disabled")
		
	def chance(self):
		num = randint(0, 4)
		for x in range(num):
			player.heal()
		
	def animate(self):
		while not self.isStopped:
			self.canvas.after(self.sleepTime)
			self.canvas.update()
			self.canvas.delete("ball")
		
			self.redisplayPlayer(self.player)
			self.redisplayDragon(self.dragon)
			
	def redisplayPlayer(self, ball):
		if ball.x > 150 or ball.x < 50:
			ball.dx = -ball.dx
			
		ball.x += ball.dx
		self.canvas.create_oval(ball.x - ball.radius, ball.y - ball.radius, ball.x + ball.radius, ball.y + ball.radius, fill = ball.color, tags = "ball")
		
	def redisplayDragon(self, ball):
		if ball.x > 350 or ball.x < 250:
			ball.dx = -ball.dx
			
		ball.x += ball.dx
		self.canvas.create_oval(ball.x - ball.radius, ball.y - ball.radius, ball.x + ball.radius, ball.y + ball.radius, fill = ball.color, tags = "ball")
		
	def getWinner(self):
		return self.winner
		
