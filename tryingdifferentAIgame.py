import numpy as np 
import pygame 
import random 

class Screen():

	def __init__(self):

		pygame.init()
		self.width, self.height = 400, 400
		self.colors = { 
						"black" : (0, 0, 0),
						"white" : (255, 255, 255),
						"red"	: (255, 0, 0),
						"green" : (0, 255, 0),
						"blue"	: (0, 0, 255),
					  }

		self.fps = 10 

		self.event = pygame.event.pump() 
		self.crash = False 

		self.display = pygame.display.set_mode((self.width, self.height))
		pygame.display.set_caption("Trying Different AI Game")
		self.clock = pygame.time.Clock() 

class Player():

	def __init__(self, Screen):

		screen = Screen()
		self.rad = 25
		pygame.draw.rect(screen.display, screen.colors["red"], (xs, ys, self.rad, self.rad), 0)

class Apple():

	def __init__(self, Screen):

		screen = Screen() 
		self.rad = 25
		pygame.draw.rect(screen.display, screen.colors["green"], (xs, ys, self.rad, self.rad), 0)

class Play():

	def __init__(self, Screen):

		




