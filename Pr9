from tkinter import *
import time
from random import randrange as rnd, random, choice
from PIL import Image, ImageTk


root = Tk()
fr = Frame(root)
root.geometry('800x600')
canv = Canvas(root, bg = 'white')
canv.pack(fill=BOTH,expand=1)
colors = ['red', 'orange', 'yellow', 'green', 'blue']

def jump2(event):
	global ball
	ball.vy = (event.y - ball.y)/15
	ball.vx = (event.x - ball.x)/15

canv.bind('<1>',jump2)

class Ball():
	def __init__(self):
		self.x = 200
		self.y = 400
		self.r = 20
		self.m = self.x
		#self.id = canv.create_oval(self.x-self.r,self.y-self.r,self.x+self.r,self.y+self.r,fill='green')
		self.images = []
		self.images.append(ImageTk.PhotoImage(Image.open('ball1.png')))
		self.images.append(ImageTk.PhotoImage(Image.open('ball2.png')))
		self.images.append(ImageTk.PhotoImage(Image.open('ball3.png')))

		self.image_number= 0
		self.rotate_frame = 20
		self.image = canv.create_image(self.x,self.y,image=self.images[self.image_number])
		self.count_from_to_rotate = 6
		
		self.vx = 0
		self.vy = 0
		self.g = 0
		self.gamer = 'man1'
	
	def move(self):
		if abs(self.vx)+abs(self.vy) > 0:
			self.rotate_frame -= 1
		if self.rotate_frame <= 0:
			self.rotate_frame = self.count_from_to_rotate
			self.image_number += 1
			if self.image_number >= len(self.images):
				self.image_number = 0
			canv.delete(self.image)
			self.image = canv.create_image(self.x,self.y,image=self.images[self.image_number])

			
		self.vy += self.g
		self.y += self.vy
		self.x += self.vx
		self.vx *= 0.99
		 
		if self.y > 550:
			self.vy *= -0.7
			self.y = 550
			self.vx *= 0.75
		
		if self.x > 750:
			self.vx *= -0.75
			self.x = 750
		
		if self.x < 50:
			self.vx *= -0.75
			self.x = 50
		
		if self.x-self.r < 400 < self.x+self.r and  self.y - self.r > 400:
			if self.x > 400:
				self.gamer = 'man1'
				man1.points += 1
				init()
			else:
				self.gamer = 'man2'
				man2.points += 1
				init()
		
		if self.y > 520:
				if ball.gamer == 'man1':
					ball.gamer = 'man2'
					init()
				else:
					ball.gamer = 'man1'
					init()
			
		if man1.x - self.r < self.x < man1.x+man1.w+self.r and man1.y-self.r < self.y < man1.y+man1.h+self.r:
			man1.lives += 1
			if man2.x - self.r < self.x < man2.x+man2.w+self.r and man2.y-self.r < self.y < man2.y+man2.h+self.r:
				man1.lives = 0
		
		if man2.x - self.r < self.x < man2.x+man2.w+self.r and man2.y-self.r < self.y < man2.y+man2.h+self.r:
			man2.lives += 1
			if man1.x - self.r < self.x < man1.x+man1.w+self.r and man1.y-self.r < self.y < man1.y+man1.h+self.r:
				man2.lives = 0
		
		if man2.lives == 3:
			man2.points += 1
			self.gamer = 'man2'
			init()
		
		if man1.lives == 3:
			man1.points += 1
			self.gamer = 'man1'
			init()
		
		
				
		#canv.coords(self.id,self.x-self.r,self.y-self.r,self.x+self.r,self.y+self.r)
		canv.coords(self.image,self.x+self.r/2,self.y+self.r/2)

		
		

class SportsMan():
	def __init__(self,left,right):
		self.x = (left+right)/2
		self.left = left
		self.right = right
		self.y = 550
		self.w = 40
		self.h = 60
		#self.id = canv.create_rectangle(self.x,self.y,self.x+self.w,self.y+self.h,fill='green',width=0)
		self.img = ImageTk.PhotoImage(Image.open('man.png'))
		self.image = canv.create_image(self.x,self.y,image=self.img)
		
		self.vx = 0
		self.ax = 0
		self.vy = 0
		self.g = 1
		self.points = 0
		self.lives = 0
		self.can_jump = True
		
	
	def move(self):
		self.vy += self.g
		self.y += self.vy 
		self.vx += self.ax
		self.x += self.vx
		self.vx *= 0.8
		
		if self.x < self.left:
			self.ax = 0
			self.vx = 0
			self.x = self.left
		
		if self.x + self.w > self.right:
			self.ax = 0
			self.vx = 0
			self.x = self.right-self.w
		
		if self.y > 550-self.h:
			self.y = 550-self.h
			self.vy = -0.7*self.vy
			self.can_jump = True
		
		if self.x - ball.r < ball.x < self.x+self.w+ball.r and self.y-ball.r < ball.y < self.y+self.h+ball.r:
			x = self.x + self.w/2
			y = self.y + self.h/2
			ball.vx = (ball.x - x)/2
			ball.vy = (ball.y - y)/2
			ball.count_from_to_rotate = (abs(ball.vx) + abs(ball.vx))/5
			while self.x - ball.r < ball.x < self.x+self.w+ball.r and self.y-ball.r < ball.y < self.y+self.h+ball.r:
				ball.x += ball.vx
				ball.y += ball.vy
			ball.g = 0.7
		
		
		
		#canv.coords(self.id,self.x,self.y,self.x+self.w,self.y+self.h)
		canv.coords(self.image,self.x+self.w/2,self.y+self.h/2)


def init():
	if ball.gamer == 'man1':
		ball.x = 200
	else:
		ball.x = 600
	canv.itemconfig(points1,text=man1.points)
	canv.itemconfig(points2,text=man2.points)
	man1.lives = 0
	man2.lives = 0
	ball.y = 450
	ball.vx = 0
	ball.vy = 0
	ball.g = 0

def new_game():
	global man1, man2, ball
	man2 = SportsMan(50,380)
	man1 = SportsMan(420,750)
	ball = Ball()
	canv.create_rectangle(50,50,750,600, width = 3)
	canv.create_line(400,400,400,600, width = 5)
	init()

def keyDown(event):
	print(event.keycode)
	keys.add(event.keycode)

def keyUp(event):
	if event.keycode in keys:
		keys.remove(event.keycode)

points1 = canv.create_text(200,300,text=0, font = "Arial 240", fill = 'lightgray')
points2 = canv.create_text(600,300,text=0, font = "Arial 240", fill = 'lightgray')

new_game()
root.bind('<Key>',keyDown)
root.bind('<KeyRelease>',keyUp)
keys = set()
while 1:
	ball.move()
	man1.move()
	man2.move()
	man1.ax = 0
	man2.ax = 0
	if 114 in keys:
		man1.ax = 4
	if 113 in keys:
		man1.ax = -4
	if 111 in keys:
		if man1.can_jump:
			man1.vy = -15
			man1.can_jump = False
	if 40 in keys:
		man2.ax = 4
	if 38 in keys:
		man2.ax = -4
	if 25 in keys:
		if man2.can_jump:
			man2.vy = -15
			man2.can_jump = False
	
	canv.update()
	time.sleep(0.03)

mainloop()