"Niklaus Parcell"
"Trying the blue square eats apple game"


#############################################
import pygame
import numpy as np  
import time
import random

#############################################

pygame.init()
width = 200
height = 200
fps = 10
points = 0
check = 0
check2 = 0

# colors 
bl = (0, 0, 0)
wh = (255, 255, 255)
r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 255)

# Display settings
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('AIgame1')
clock = pygame.time.Clock()

# Characters in game
rad = 25
thi = 0  # if 0, rectangle filled
def one(xs, ys):
	pygame.draw.rect(display, r, (xs,ys,rad,rad), thi)
def two(xs, ys):
	pygame.draw.rect(display, b, (xs,ys,rad,rad), thi)
def app(xs, ys):
	pygame.draw.rect(display, g, (xs,ys,rad,rad), thi)

def how_far(xm, ym, xa, ya):  # m is position of mover, a is position of the apple
	xn, yn = abs(xm - xa), abs(ym - ya)
	return xn, yn



# Event
event = pygame.event.pump()

# Positioning stuff
x_change = 0
y_change = 0
x, y = 0, 0
x1, y1 = random.randrange(0, width, rad), random.randrange(0, height, rad)
x2, y2 = random.randrange(0, width, rad), random.randrange(0, height, rad)
xg, yg = random.randrange(0, width, rad), random.randrange(0, height, rad)

# Loop
crash = False
while not crash:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crash = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_x:
				crash = True
			# if event.key == pygame.K_UP:
			# 	y -= rad
			# if event.key == pygame.K_DOWN:
			# 	y += rad 
			# if event.key == pygame.K_LEFT:
			# 	x -= rad 
			# if event.key == pygame.K_RIGHT:
			# 	x += rad 

	# Conditions
	"1) Set up move to the thing"
	# if check == 0:
	# 	x_n = -(x - xg)
	# 	y_n = -(y - yg)
	# if check == 1:
	# 	x_n = -(x - xg)
	# 	y_n = -(y - xg)

	# if x_n < 0:
	# 	x_change = -rad 
	# if x_n > 0:
	# 	x_change = rad
	# if x_n == 0:
	# 	x_change = 0

	# y_n = -(y - yg)
	# if y_n < 0:
	# 	y_change = -rad 
	# if y_n > 0:
	# 	y_change = rad
	# if y_n == 0:
		# y_change = 0
		

	"Boundaries"
	# if x <= 0:
	# 	x_change = 0
	# 	x += rad 
	# if x >= width:
	# 	x_change = 0
	# 	x -= rad
	# if y <= 0:
	# 	y_change = 0
	# 	y += rad
	# if y >= height:
	# 	y_change = 0
		# y -= rad 

	# If apple collected
	if x > xg-rad and x < xg+rad and y > yg-rad and y < yg+rad:
		xg = random.randrange(rad, width-rad, rad) 
		yg = random.randrange(rad, height-rad, rad) 
		points += 1

	# if x != 0 and y != 0:
	# 	check = random.randrange(0, 2, 1)
	# 	if check == 0:
	# 		x_change = 0
	# 	if check == 1:
	# 		y_change = 0

	# Randomly generate more apples
	x_n, y_n = -(x - xg), -(y - yg)  # tells it where to go
	if x_n < 0:  # x_changes
		x_change = -rad 
	if x_n > 0:
		x_change = rad
	if x_n == 0:
		x_change = 0
	y_n = -(y - yg)  # x_changes
	if y_n < 0:
		y_change = -rad 
	if y_n > 0:
		y_change = rad
	if y_n == 0:
		y_change = 0
	if x != 0 and y != 0:  # one axis at a time
		check = random.randrange(0, 2, 1)
		if check == 0:
			x_change = 0
		if check == 1:
			y_change = 0

	display.fill(bl)
	app(xg, yg)
	x += x_change
	y += y_change
	one(x, y)

	# Makes them move one at a time
	

	one(x1, y1)
	two(x2, y2)
	pygame.display.flip()
	clock.tick(fps)

pygame.quit()
quit()