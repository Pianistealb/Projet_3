
"""
Class Character for Mac Gyver Labyrinth Game
Amandine Le Bras
"""

import pygame
from pygame.locals import *

from constantes import *
from C_Object import *
from C_Labyrinth import *



class Character:
	"""Class to create a character"""

	def __init__(self, right, left, up, down, labyrinth):
		"""This constructor define the instance for Macgyver position,
		movement and the picture layout for his movement"""

		self.right = pygame.image.load(right).convert_alpha()
		self.left = pygame.image.load(left).convert_alpha()
		self.up = pygame.image.load(up).convert_alpha()
		self.down = pygame.image.load(down).convert_alpha()
		#Character position in boxes and pixels
		self.case_x = 0
		self.case_y = 0
		self.x = 0
		self.y = 0
		#Default direction
		self.direction = self.right
		#Level in which the character is located 
		self.labyrinth = labyrinth
		self.found = 0

	def move(self, direction):
		"""Method for moving the character"""	

		#Move to the right
		if direction == 'right':
			#Not to exceed the screen
			if self.case_x < (NUMBER_SPITE_COT - 1):
				#We check that the destination box is not a wall
				if self.labyrinth.structure[self.case_y][self.case_x+1] not in {'m' , 'g'}:
					#Moving a case
					self.case_x += 1
					#Calculation of the "real" position in pixels
					self.x = self.case_x * SIZE_SPRITE
			#Image in the right direction
			self.direction = self.right
			# check if the resultant position is an object
			if self.labyrinth.structure[self.case_y][self.case_x] in 'o1':
				# tag the sprite with the object
				self.labyrinth.structure[self.case_y][self.case_x] = 'i1'
				self.found += 1		
			elif self.labyrinth.structure[self.case_y][self.case_x] in 'o2':
				self.labyrinth.structure[self.case_y][self.case_x] = 'i2'
				self.found += 1
			elif self.labyrinth.structure[self.case_y][self.case_x] in 'o3':
				self.labyrinth.structure[self.case_y][self.case_x] = 'i3'
				self.found += 1
			elif self.labyrinth.structure[self.case_y][self.case_x] in 'a' and self.found == 3:
				self.labyrinth.structure[self.case_y][self.case_x] = 'v'
				
		#Moving to the left
		if direction == 'left':
			if self.case_x > 0:
				if self.labyrinth.structure[self.case_y][self.case_x-1] not in {'m' , 'g'}:
					self.case_x -= 1
					self.x = self.case_x * SIZE_SPRITE
			self.direction = self.left
			# check if the resultant position is an object
			if self.labyrinth.structure[self.case_y][self.case_x] in 'o1':
				# tag the sprite with the object
				self.labyrinth.structure[self.case_y][self.case_x] = 'i1'
				self.found += 1			
			elif self.labyrinth.structure[self.case_y][self.case_x] in 'o2':
				self.labyrinth.structure[self.case_y][self.case_x] = 'i2'
				self.found += 1				
			elif self.labyrinth.structure[self.case_y][self.case_x] in 'o3':
				self.labyrinth.structure[self.case_y][self.case_x] = 'i3'
				self.found += 1
			elif self.labyrinth.structure[self.case_y][self.case_x] in 'a' and self.found == 3:
				self.labyrinth.structure[self.case_y][self.case_x] = 'v'

		#Moving to the up
		if direction == 'up':
			if self.case_y > 0:
				if self.labyrinth.structure[self.case_y-1][self.case_x] not in {'m' , 'g'}:
					self.case_y -= 1
					self.y = self.case_y * SIZE_SPRITE
			self.direction = self.up
			# check if the resultant position is an object
			if self.labyrinth.structure[self.case_y][self.case_x] in 'o1':
				# tag the sprite with the object
				self.labyrinth.structure[self.case_y][self.case_x] = 'i1'
				self.found += 1
			elif self.labyrinth.structure[self.case_y][self.case_x] in 'o2':
				self.labyrinth.structure[self.case_y][self.case_x] = 'i2'
				self.found += 1
			elif self.labyrinth.structure[self.case_y][self.case_x] in 'o3':
				self.labyrinth.structure[self.case_y][self.case_x] = 'i3'
				self.found += 1
			elif self.labyrinth.structure[self.case_y][self.case_x] in 'a' and self.found == 3:
				self.labyrinth.structure[self.case_y][self.case_x] = 'v'
				
		#Moving to the down
		if direction == 'down':
			if self.case_y < (NUMBER_SPITE_COT - 1):
				if self.labyrinth.structure[self.case_y+1][self.case_x] not in {'m' , 'g'}:
					self.case_y += 1
					self.y = self.case_y * SIZE_SPRITE
			self.direction = self.down
			# check if the resultant position is an object
			if self.labyrinth.structure[self.case_y][self.case_x] in 'o1':
				# tag the sprite with the object
				self.labyrinth.structure[self.case_y][self.case_x] = 'i1'
				self.found += 1			
			elif self.labyrinth.structure[self.case_y][self.case_x]in 'o2':
				self.labyrinth.structure[self.case_y][self.case_x] = 'i2'
				self.found += 1
			elif self.labyrinth.structure[self.case_y][self.case_x] in 'o3':
				self.labyrinth.structure[self.case_y][self.case_x] = 'i3'
				self.found += 1
			elif self.labyrinth.structure[self.case_y][self.case_x] in 'a' and self.found == 3:
				self.labyrinth.structure[self.case_y][self.case_x] = 'v'
