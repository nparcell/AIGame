"Niklaus Parcell"
"Adapted from AIGame3"

import pygame 
import numpy as np 
import time 
import random 

class game():

	def __init__(self):

		pygame.init()
		self.ascript = 'AIGame5_play.py'  # abstraction
		self.title = 'AIGame5'
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
		self.xs, self.ys = 0, 0
		self.xs_red, self.ys_red = 0, 0
		self.xs_blue, self.ys_blue = 0, 0
		self.zap_width_red, self.zap_width_blue = 0, 0
		self.zap_height_red, self.zap_height_blue = 0, 0

	def colors(self):
		
		"""
		Colors for the game, i.e. player colors, zapper colorss, background, etc.
		"""

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
		self.myFont = pygame.font.SysFont("Times New Roman", self.rad)

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
		
		self.x_player_1, self.y_player_1 = random.randrange(0, self.width, self.rad), random.randrange(0, self.height, self.rad)

	def reset_player_2(self):
		
		self.x_player_2, self.y_player_2 = random.randrange(0, self.width, self.rad), random.randrange(0, self.height, self.rad)

	def outside_boundary(self, x, y, points):

		if x < -10 or x > self.width or y < 0 or y > self.height:
			if x == self.x_player_1 or y == self.y_player_1:
				game.reset_player_1(self)
				self.points1 -= 1
			if x == self.x_player_2 or y == self.y_player_2:
				game.reset_player_2(self)
				self.points2 -= 1

	def dont_change_pos(self, x_change, y_change):

		x_change, y_change = 0, 0
		return x_change, y_change 

	def zap_check_1(self):

		""" Only want player to reset if zapped, not if can_zap == 1
		"""

		game.zap_red(self, self.xs_red, self.ys_red)
		game.reset_player_2(self)
		game.dont_change_pos(self, self.x_change_1, self.y_change_1)
		self.points1 += 1

	def zap_check_2(self):

		game.zap_blue(self, self.xs_blue, self.ys_blue)
		game.reset_player_1(self)		
		game.dont_change_pos(self, self.x_change_2, self.y_change_2)
		self.points2 += 1

	def zap_1_left(self):

		self.zap_width_red = abs(self.x_player_1 - self.x_player_2)
		self.zap_height_red = self.rad 
		self.xs_red = self.x_player_2 
		self.ys_red = self.y_player_1
		game.zap_red(self, self.xs_red, self.ys_red)

	def zap_1_right(self):

		self.zap_width_red = abs(self.x_player_1 - self.x_player_2)
		self.zap_height_red = self.rad 
		self.xs_red = self.x_player_1 + self.rad
		self.ys_red = self.y_player_1 
		game.zap_red(self, self.xs_red, self.ys_red)

	def zap_1_up(self):

		self.zap_width_red = self.rad 
		self.zap_height_red = abs(self.y_player_1 - self.y_player_2)
		self.xs_red = self.x_player_1 
		self.ys_red = self.y_player_2 
		game.zap_red(self, self.xs_red, self.ys_red)

	def zap_1_down(self):

		self.zap_width_red = self.rad 
		self.zap_height_red = abs(self.y_player_1 - self.y_player_2)
		self.xs_red = self.x_player_1 
		self.ys_red = self.y_player_1 + self.rad 
		game.zap_red(self, self.xs_red, self.ys_red)

	def zap_2_left(self):

		self.zap_width_blue = abs(self.x_player_2 - self.x_player_1)
		self.zap_height_blue = self.rad 
		self.xs_blue = self.x_player_1
		self.ys_blue = self.y_player_2 
		game.zap_blue(self, self.xs_blue, self.ys_blue)

	def zap_2_right(self):

		self.zap_width_blue = abs(self.x_player_2 - self.x_player_1)
		self.zap_height_blue = self.rad 
		self.xs_blue = self.x_player_2 + self.rad 
		self.ys_blue = self.y_player_2 
		game.zap_blue(self, self.xs_blue, self.ys_blue)

	def zap_2_up(self):

		self.zap_width_blue = self.rad 
		self.zap_height_blue = abs(self.y_player_1 - self.y_player_2)
		self.xs_blue = self.x_player_2 
		self.ys_blue = self.y_player_1 
		game.zap_blue(self, self.xs_blue, self.ys_blue)

	def zap_2_down(self):

		self.zap_width_blue = self.rad 
		self.zap_height_blue = abs(self.y_player_1 - self.y_player_2)
		self.xs_blue = self.x_player_2 
		self.ys_blue = self.y_player_2 + self.rad 
		game.zap_blue(self, self.xs_blue, self.ys_blue)

	def zap(self):  # *** Need to make this different, the program needs to zap and then see what happens. All it should know is that the sprite for the zapper appears above the character for the visual effect. 

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
				game.zap_check_1(self)
			if self.y_player_2 == self.y_player_1:
				self.zap_height_red = self.rad 
				self.ys_red = self.y_player_1 
				self.zap_width_red = abs(self.x_player_1 - self.x_player_2)
				if self.x_player_1 - self.x_player_2 > 0: # zap left
					self.xs_red = self.x_player_2 
				if self.x_player_1 - self.x_player_2 < 0: # zap right   
					self.xs_red = self.x_player_1 + self.rad 
				game.zap_check_1(self)
		if can_zap == 2:
			if self.x_player_1 == self.x_player_2:
				self.zap_width_blue = self.rad 
				self.xs_blue = self.x_player_2 
				self.zap_height_blue = abs(self.y_player_1 - self.y_player_2)
				if self.y_player_2 - self.y_player_1 > 0: # zap up 
					self.ys_blue = self.y_player_1
				if self.y_player_2 - self.y_player_1 < 0: # zap down 
					self.ys_blue = self.y_player_2 + self.rad
				game.zap_check_2(self)
			if self.y_player_2 == self.y_player_1:
				self.zap_height_blue = self.rad 
				self.ys_blue = self.y_player_2 
				self.zap_width_blue = abs(self.x_player_2 - self.x_player_1)
				if self.x_player_2 - self.x_player_1 > 0: # zap left 
					self.xs_blue = self.x_player_1
				if self.x_player_2 - self.x_player_1 < 0: # zap right 
					self.xs_blue = self.x_player_2 + self.rad
				game.zap_check_2(self)

	def how_far(self, x_player, y_player, x_apple, y_apple):  # *** Probably good to know where the apple is right? This could be part of what the data collects. 
		xn, yn = abs(x_player - x_apple), abs(y_player - y_apple)
		return xn, yn

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

	def red_move_blue_waits(self, x, y, x_change, y_change):
		x_n, y_n = -(x - self.x_apple), -(y- self.y_apple)
		if x_n < 0:
			x_change = -self.rad
		if x_n > 0:
			x_change = self.rad
		if x_n == 0:
			x_change = 0
		if y_n < 0:
			y_change =  -self.rad
		if y_n > 0:
			y_change = self.rad
		if y_n == 0:
			y_change = 0
		if x == self.x_player_1 and y == self.y_player_1:
			self.x_change_1, self.y_change_1 = x_change, y_change 
		if x == self.x_player_2 and y == self.y_player_2:
			self.x_change_2, self.y_change_2 = x_change, y_change 

		return x_change, y_change 

	def setup_matrix(self):

		self.list_positions = [self.x_player_1, self.y_player_1, self.x_player_2, self.y_player_2, self.x_apple, self.y_apple]
		return self.list_positions

	def random_function(self):

		return random.randint(0, 15)
	
	def decisions(self, number):

		if number == 1:
			self.x_change_1 = -self.rad 
		if number == 0:
			self.x_change_1 = self.rad 
		if number == 2:
			self.y_change_1 = -self.rad 
		if number == 3:
			self.y_change_1 = self.rad 
		if number == 4:
			self.x_change_2 = -self.rad 
		if number == 5:
			self.x_change_2 = self.rad 
		if number == 6:
			self.y_change_2 = -self.rad 
		if number == 7:
			self.y_change_2 = self.rad 
		if number == 8:
			game.zap_1_left(self)
		if number == 9:
			game.zap_1_right(self)
		if number == 10:
			game.zap_1_up(self)
		if number == 11:
			game.zap_1_down(self)
		if number == 12:
			game.zap_2_left(self)
		if number == 13:
			game.zap_2_right(self)
		if number == 14: 
			game.zap_2_up(self)
		if number == 15:
			game.zap_2_down(self)


def Play(self):
	crash = False 
	while not crash:
		for self.event in pygame.event.get():
			if self.event.type == pygame.QUIT:
				crash = True
			if self.event.type == pygame.KEYDOWN:
				if self.event.key == pygame.K_x:
					crash = True

		game.if_apple_collected(self, self.x_player_1, self.y_player_1, self.x_apple, self.y_apple)
		game.if_apple_collected(self, self.x_player_2, self.y_player_2, self.x_apple, self.y_apple)

		game.decisions(self, game.random_function(self))
		game.one_axis_at_a_time(self)
		game.check_next_to(self)
		game.thing_plus_equals_change(self)
		# game.zap(self)

		game.outside_boundary(self, self.x_player_1, self.y_player_1, self.points1)
		game.outside_boundary(self, self.x_player_2, self.y_player_2, self.points2)

		self.display.fill(self.black)
		game.apple(self, self.x_apple, self.y_apple)
		game.player1(self, self.x_player_1, self.y_player_1)
		game.player2(self, self.x_player_2, self.y_player_2)
		# game.zap_red(self, self.xs_red, self.ys_red)
		# game.zap_blue(self, self.xs_blue, self.ys_blue)

		# Display points
		game.score_board(self)

		# print(game.setup_matrix(self))
		
		pygame.display.flip()
		self.clock.tick(self.fps)
