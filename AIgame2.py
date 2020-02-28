"Niklaus Parcell"
"Trying the blue square eats apple game"


############################################################################
import pygame
import numpy as np  
import time
import random

############################################################################

pygame.init()
width = 400
height = 200
fps = 200  # frames per second
points, points2 = 0, 0  # track points
check, check1, check2 = 0, 0, 0
forone, fortwo = 0, 0  # checkpoints 
moves1, moves2 = 0, 0  # count who moves (factors in to win)
whowins1, whowins2 = 0, 0  # to count who wins
block1, block2 = 0, 0 

# colors 
bl = (0, 0, 0)
wh = (255, 255, 255)
r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 255)

# Display settings
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('AIgame2')
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
x_change, x_change2 = 0, 0
y_change, y_change2 = 0, 0
x, y, x2, y2, = 0, 0, width-rad, height-rad
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

####### Conditions ##########################################################

	"If apple collected"
	"1) Red figure (one) eats apple"
	if x > xg-rad and x < xg+rad and y > yg-rad and y < yg+rad:
		xg = random.randrange(rad, width-rad, rad) 
		yg = random.randrange(rad, height-rad, rad) 
		points += 1
	"2) Blue figure (two) eats apple"
	if x2 > xg-rad and x2 < xg+rad and y2 > yg-rad and y2 < yg+rad:
		xg = random.randrange(rad, width-rad, rad)
		yg = random.randrange(rad, height-rad, rad)
		points2 += 1

	"Red moves, blue waits"
	check1, check2 = random.uniform(0, 2), random.uniform(0, 2)
	forone, fortwo = check1, check2
	if forone < fortwo:  
		x_n, y_n = -(x - xg), -(y - yg)  # tells it where to go
		if x_n < 0:  # x_changes
			x_change, x_change2 = -rad, 0
		if x_n > 0:
			x_change, x_change2 = rad, 0
		if x_n == 0:
			x_change, x_change2 = 0, 0
		y_n = -(y - yg)
		if y_n < 0:
			y_change, y_change2 = -rad, 0
		if y_n > 0:
			y_change, y_change2 = rad, 0
		if y_n == 0:
			y_change, y_change2 = 0, 0
		if x != 0 and y != 0:  # one axis at a time
			check = random.randrange(0, 2, 1)
			if check == 0:
				x_change = 0
			if check == 1:
				y_change = 0
		moves1 += 1
		"Blue moves, red waits"
	if fortwo < forone:  
		x_n2, y_n2 = -(x2 - xg), -(y2 - yg)  # tells it where to go
		if x_n2 < 0:  # x_changes
			x_change = 0
			x_change2 = -rad
		if x_n2 > 0:
			x_change = 0
			x_change2 = rad
		if x_n2 == 0:
			x_change, x_change2 = 0, 0
		y_n2 = -(y2 - yg)
		if y_n2 < 0:
			y_change, y_change2 = -0, -rad 
		if y_n2 > 0:
			y_change, y_change2 = 0, rad 
		if y_n2 == 0:
			y_change, y_change2 = 0, 0
		if x2 != 0 and y2 != 0:  # one axis at a time
			check = random.randrange(0, 2, 1)
			if check == 0:
				x_change2 = 0
			if check == 1:
				y_change2 = 0
		moves2 += 1
	if fortwo == forone:
		pass

	x += x_change
	y += y_change
	x2 += x_change2
	y2 += y_change2

	choose_rand = random.randint(0, 1)
	"Red blocks blue"
	if x == xg and x2 == xg and y2 - y == 0:
		y2 -= y_change2
		block1 += 1
		if choose_rand == 0:
			x2 -= x_change2 
		if choose_rand == 1:
			x2 -= x_change2 
	if y == yg and y2 == yg and x2 - x == 0:
		x2 -= x_change2
		block1 += 1
		if choose_rand == 0:
			y2 -= y_change2 
		if choose_rand == 1:
			y2 -= y_change2 
		
	"Blue blocks red"
	if x2 == xg and x == xg and y - y2 == 0:
		y -= y_change
		block2 += 1
		if choose_rand == 0:
			x -= x_change 
		if choose_rand == 1:
			x -= x_change
	if y2 == yg and y == yg and x - x2 == 0:
		x -= x_change 
		block2 += 1
		if choose_rand == 0:
			y -= y_change
		if choose_rand == 1:
			y -= y_change 

	display.fill(bl)
	app(xg, yg)
	
	one(x, y)
	two(x2, y2)

	pygame.display.flip()
	clock.tick(fps)

if points != 0 and points2 != 0:
	whowins1, whowins2 = (moves1/points)*block1, (moves2/points2)*block2
print("red moved: ", moves1)
print("blue moved: ", moves2)
print("Red blocked blue", block1, "times")
print("Blue blocked red", block2, "times")

if points != 0 and points2 != 0:
	print("points for red: ", points)
	print("points for blue: ", points2)
print("")
print("Whoever moves less with more points wins")
print("Blocks are deductions")
print("")
if whowins1 < whowins2:
	print("Red wins")
if whowins2 < whowins1:
	print("Blue wins")
pygame.quit()
quit()