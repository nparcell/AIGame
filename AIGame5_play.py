import AIGame5
import pygame 

a = AIGame5.game()
a.colors()
a.display_settings()
a.generate_positions_of_apple()

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
		a.zap_1_left()
	if number == 9:
		a.zap_1_right()
	if number == 10:
		a.zap_1_up()
	if number == 11:
		a.zap_1_down()
	if number == 12:
		a.zap_2_left()
	if number == 13:
		a.zap_2_right()
	if number == 14: 
		a.zap_2_up()
	if number == 15:
		a.zap_2_down()

AIGame5.Play(a)