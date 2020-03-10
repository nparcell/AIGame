"Niklaus Parcell"
"Trying the blue square eats apple game"
"Attempting to adapt code from AIGame2.py in to object-oriented code"

import pygame 
import numpy as np 
import time 
import random 

class game_properties():

	def __init__(self):

		pygame.init()
		self.title = 'AIGame3'
		self.width = 400
		self.height = 400 
		self.fps = 15  # fps 
		self.points1, self.points2 = 0, 0  # both players start at 2 points 
		self.check, self.check1, self.check2 = 0, 0, 0
		self.forone, self.fortwo = 0, 0
		self.moves1, self.moves2 = 0, 0  # track how many moves each player has 
		self.whowins1, self.whowins2 = 0, 0  # see who wins 
		self.block1, self.block2 = 0, 0  # track who blocks who 

		# Player character properties
		self.rad = 25
		self.thickness = 0  # fills in the square
		self.x_change_1, self.x_change_2 = 0, 0
		self.y_change_1, self.y_change_2 = 0, 0		

		# Starting positions of players 
		self.x_player_1, self.y_player_1, self.x_player_2, self.y_player_2 = 0, 0, self.width - self.rad, self.height - self.rad
		self.xs, self.ys = 0, 0

		# Other game props 
		self.crash = False
		self.event = pygame.event.pump()

	def colors(self):

		self.black = (0, 0, 0)
		self.white = (255, 255, 255)
		self.red = (255, 0, 0)
		self.green = (0, 255, 0)
		self.blue = (0, 0, 255)
		self.moccasin = (255, 228, 181)
		self.cornflower_blue = (100, 149, 237)
		self.salmon = (250, 128, 114)

	def display_settings(self):

		self.display = pygame.display.set_mode((self.width, self.height))
		pygame.display.set_caption(str(self.title))
		self.clock = pygame.time.Clock()
		self.myFont = pygame.font.SysFont("Times New Roman", 25)

	def player1(self, xs, ys):

		pygame.draw.rect(self.display, self.red, (xs, ys, self.rad, self.rad), self.thickness)

	def player2(self, xs, ys):

		pygame.draw.rect(self.display, self.blue, (xs, ys, self.rad, self.rad), self.thickness)

	def apple(self, xs, ys):

		pygame.draw.rect(self.display, self.green, (xs, ys, self.rad, self.rad), self.thickness)

	def zapper(self, xs, ys):

		pygame.draw.rect(self.display, self.moccasin, (xs, ys, self.zap_width, self.zap_height), self.thickness)

	def zap_blue(self, xs, ys):

		pygame.draw.rect(self.display, self.cornflower_blue, (xs, ys, self.zap_width_blue, self.zap_height_blue), self.thickness)

	def zap_red(self, xs, ys):

		pygame.draw.rect(self.display, self.salmon, (xs, ys, self.zap_width_red, self.zap_height_red), self.thickness)
				
	def check_next_to(self):

		cant_move = random.randint(1, 2)
		up_or_down = random.randint(0, 1)
		if up_or_down == 0:
			move = -self.rad
		if up_or_down == 1:
			move = self.rad  
		if self.x_player_1 == self.x_player_2:
			if cant_move == 1 and abs(self.y_player_1 - self.y_player_2) == self.rad:
				self.x_change_1 = move 
			if cant_move == 2 and abs(self.y_player_1 - self.y_player_2) == self.rad:
				self.x_change_2 = move 
		if self.y_player_1 == self.y_player_2:
			if cant_move == 1 and abs(self.x_player_1 - self.x_player_2) == self.rad:
				self.y_change_1 = move 
			if cant_move == 2 and abs(self.x_player_1 - self.x_player_2) == self.rad:
				self.y_change_2 = move 


	def reset_player_1(self):
		
		self.x_player_1, self.y_player_1 = 0, self.height/2 

	def reset_player_2(self):
		
		self.x_player_2, self.y_player_2 = self.width - self.rad, self.height / 2

	def dont_change_pos_2(self):

		self.x_change_2, self.y_change_2 = 0, 0

	def dont_change_pos_1(self):

		self.x_change_1, self.y_change_1 = 0, 0

	def zap_check_1(self):

		""" Only want player to reset if zapped, not if can_zap == 1
		"""

		game_properties.zap_red(self, self.xs_red, self.ys_red)
		game_properties.reset_player_2(self)
		game_properties.dont_change_pos_1(self)

	def zap_check_2(self):

		game_properties.zap_blue(self, self.xs_blue, self.ys_blue)
		game_properties.reset_player_1(self)		
		game_properties.dont_change_pos_2(self)

	def zap(self):

		# Condition if player 1 or 2 has power to zap
		can_zap = random.randint(1, 15)
		self.xs, self.ys = 0, 0
		self.xs_red, self.ys_red = 0, 0
		self.xs_blue, self.ys_blue = 0, 0
		self.zap_width_red, self.zap_width_blue = 0, 0
		self.zap_height_red, self.zap_height_blue = 0, 0

		# Check position relative to other player
		if can_zap == 1:
			if self.x_player_2 == self.x_player_1:
				self.zap_width_red = self.rad 
				self.xs_red = self.x_player_1
				self.zap_height_red = abs(self.y_player_1 - self.y_player_2)
				if self.y_player_1 - self.y_player_2 > 0: # zap up
					self.ys_red = self.y_player_2
				if self.y_player_1 - self.y_player_2 < 0: # zap down 
					self.ys_red = self.y_player_1 + self.rad 
				game_properties.zap_check_1(self)
			if self.y_player_2 == self.y_player_1:
				self.zap_height_red = self.rad 
				self.ys_red = self.y_player_1 
				self.zap_width_red = abs(self.x_player_1 - self.x_player_2)
				if self.x_player_1 - self.x_player_2 > 0: # zap left
					self.xs_red = self.x_player_2 
				if self.x_player_1 - self.x_player_2 < 0: # zap right   
					self.xs_red = self.x_player_1 + self.rad 
				game_properties.zap_check_1(self)
		if can_zap == 2:
			if self.x_player_1 == self.x_player_2:
				self.zap_width_blue = self.rad 
				self.xs_blue = self.x_player_2 
				self.zap_height_blue = abs(self.y_player_1 - self.y_player_2)
				if self.y_player_2 - self.y_player_1 > 0: # zap up 
					self.ys_blue = self.y_player_1
				if self.y_player_2 - self.y_player_1 < 0: # zap down 
					self.ys_blue = self.y_player_2 + self.rad
				game_properties.zap_check_2(self)
			if self.y_player_2 == self.y_player_1:
				self.zap_height_blue = self.rad 
				self.ys_blue = self.y_player_2 
				self.zap_width_blue = abs(self.x_player_2 - self.x_player_1)
				if self.x_player_2 - self.x_player_1 > 0: # zap left 
					self.xs_blue = self.x_player_1
				if self.x_player_2 - self.x_player_1 < 0: # zap right 
					self.xs_blue = self.x_player_2 + self.rad
				game_properties.zap_check_2(self)
			

	def how_far(self, x_player, y_player, x_apple, y_apple):
		xn, yn = abs(x_player - x_apple), abs(y_player - y_apple)
		return xn, yn 

	def generate_positions_of_apple(self):
		self.x_apple, self.y_apple = random.randrange(0, self.width, self.rad), random.randrange(0, self.height, self.rad)

	def if_apple_collected(self, x_player, y_player, x_apple, y_apple):
		if x_player > x_apple - self.rad and x_player < x_apple + self.rad and y_player > y_apple - self.rad and y_player < y_apple + self.rad:
			self.x_apple = random.randrange(self.rad, self.width - self.rad, self.rad)
			self.y_apple = random.randrange(self.rad, self.height - self.rad, self.rad)
			if x_player == self.x_player_1 and y_player == self.y_player_1:
				self.points1 += 1
			if x_player == self.x_player_2 and y_player == self.y_player_2:
				self.points2 += 1

	def red_move_blue_waits(self):
		self.forone, self.fortwo = random.uniform(0, 2), random.uniform(0, 2)
		if self.forone < self.fortwo:
			x_n, y_n = -(self.x_player_1 - self.x_apple), -(self.y_player_1 - self.y_apple)
			if x_n < 0:
				self.x_change_1, self.x_change_2 = -self.rad, 0
			if x_n > 0:
				self.x_change_1, self.x_change_2 = self.rad, 0
			if x_n == 0:
				self.x_change_1, self.x_change_2 = 0, 0
			if y_n < 0:
				self.y_change_1, self.y_change_2 = -self.rad, 0
			if y_n > 0:
				self.y_change_1, self.y_change_2 = self.rad, 0
			if y_n == 0:
				self.y_change_1, self.y_change_2 = 0, 0
		if self.forone > self.fortwo:
			x_n2, y_n2 = -(self.x_player_2 - self.x_apple), - (self.y_player_2 - self.y_apple)
			if x_n2 < 0:
				self.x_change_1, self.x_change_2 = 0, -self.rad
			if x_n2 > 0:
				self.x_change_1, self.x_change_2 = 0, self.rad
			if x_n2 == 0:
				self.x_change_1, self.x_change_2 = 0, 0
			if y_n2 < 0:
				self.y_change_1, self.y_change_2 = 0, -self.rad 
			if y_n2 > 0:
				self.y_change_1, self.y_change_2 = 0, self.rad 
			if y_n2 == 0:
				self.y_change_1, self.y_change_2 = 0, 0
		if self.forone == self.fortwo:
			pass 

	def one_axis_at_a_time(self):

		check = random.randint(0, 1)
		if self.x_player_1 != 0 and self.y_player_1 != 0:
			if check == 0:
				self.x_change_1 = 0
			if check == 1:
				self.y_change_1 = 0
		if self.x_player_2 != 0 and self.y_player_2 != 0:
			if check == 0:
				self.x_change_2 = 0
			if check == 1:
				self.y_change_2 = 0

	def thing_plus_equals_change(self):
		self.x_player_1 += self.x_change_1 
		self.y_player_1 += self.y_change_1
		self.x_player_2 += self.x_change_2
		self.y_player_2 += self.y_change_2

	def score_board(self):

		self.disp_points_1 = self.myFont.render(str(self.points1), 1, self.red)
		self.disp_points_2 = self.myFont.render(str(self.points2), 1, self.blue)
		self.display.blit(self.disp_points_1, (self.rad - 5, self.height-self.rad - 5))
		self.display.blit(self.disp_points_2, (self.width - self.rad - 20, self.height - self.rad - 5))

class learn():

	def __init__(self):

		self.x, self.y = 0, 0

	def nonlin(x, deriv = False):
		if(deriv == True):
			return x*(1-x)

		return 1/(1+np.exp(-x))

def Play(self):
	crash = False 
	while not crash:
		for self.event in pygame.event.get():
			if self.event.type == pygame.QUIT:
				crash = True
			if self.event.type == pygame.KEYDOWN:
				if self.event.key == pygame.K_x:
					crash = True

		game_properties.if_apple_collected(self, self.x_player_1, self.y_player_1, self.x_apple, self.y_apple)
		game_properties.if_apple_collected(self, self.x_player_2, self.y_player_2, self.x_apple, self.y_apple)

		game_properties.red_move_blue_waits(self)
		game_properties.one_axis_at_a_time(self)
		game_properties.check_next_to(self)
		game_properties.thing_plus_equals_change(self)
		game_properties.zap(self)

		self.display.fill(self.black)
		game_properties.apple(self, self.x_apple, self.y_apple)
		game_properties.player1(self, self.x_player_1, self.y_player_1)
		game_properties.player2(self, self.x_player_2, self.y_player_2)
		game_properties.zap_red(self, self.xs_red, self.ys_red)
		game_properties.zap_blue(self, self.xs_blue, self.ys_blue)

		# Display points
		game_properties.score_board(self)
		
		pygame.display.flip()
		self.clock.tick(self.fps)

