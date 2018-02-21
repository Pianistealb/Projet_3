"""
Class for Mac Gyver Labyrinth Game
Amandine Le Bras
"""

# -tc- De manière générale, ce serait plus clair de mettre les classes dans des modules
# -tc- dédiés que dans un module "fourre-tout" comme classes.py.

import pygame
import random
from pygame.locals import *

from constantes import *


class Labyrinth:
    """-tc- Ce serait une bonne pratique de donner également une docstring à la classe."""

	def __init__(self, file):
        """-tc- Donner également une docstring au constructeur."""
		self.file = file
		self.structure = 0

	def generate (self):
		"""Loading labyrinth with the file
		Creact a list principal, contene a list for line loading"""	
		#open file
        # -tc- file est un mot réservé du langage
		with open(self.file, "r") as file:
			structure_lab = []
			#we go through the letters contained in the file
			for line in file:
				line_lab = []
				for sprite in line:
					#to add the sprite to the list of th line
					line_lab.append(sprite)
				#We add the line for the liste in the labyrinth
				structure_lab.append(line_lab)
			#Save this structure
			self.structure = structure_lab

	def display(self, window):
		"""Method to display the level according to
		of the structure list returned by generer () """
		#display the pictures 
		# load the image
		wall_origine = pygame.image.load(PICTURE_START).convert()
		wall = pygame.image.load(PICTURE_WALL).convert_alpha()
		murdoc = pygame.image.load(PICTURE_MURDOC).convert_alpha()
		
        # -tc- La manière pythonique de faire est: for num_line, line in enumerate(self.structure):
		num_line = 0
		for line in self.structure:
			#We go through the lists of lines
            # -tc- La manière pythonique de faire est: for num_case, sprite in enumerate(line):
			num_case = 0
			for sprite in line:
				#The actual position in pixels is calculated
				x = num_case * SIZE_SPRITE
				y = num_line * SIZE_SPRITE
				if sprite == 'm':		   #m = Wall
					window.blit(wall, (x,y))
				elif sprite == 'd':		   #d = Start
					window.blit(wall_origine, (x,y))
				elif sprite == 'a':		   #a = Murdoc
					window.blit(murdoc, (x,y))
                # -tc- L'avantage, si tu utilises enumerate(), c'est que tu n'as plus besoin de mettre 
                # -tc- à jour num_case et num_line
				num_case += 1
			num_line += 1

class Character:
	"""Class to create a character"""
	def __init__(self, right, left, up, down, labyrinth):
        """-tc- Ajouter une doctring à cette méthode"""
		self.right = pygame.image.load(right).convert_alpha()
		self.left = pygame.image.load(left).convert_alpha()
		self.up = pygame.image.load(up).convert_alpha()
		self.down = pygame.image.load(down).convert_alpha()
		#Character position in boxes and pixels
        # -tc- Je pense qu'il n'y a pas besoin d'avoir (case_x, case_y) et (x, y), l'un étant calculé
        # -tc- à partir de l'autre.
        # -tc- On peut utiliser le décorateur @property pour définir self.x et self.y
		self.case_x = 0
		self.case_y = 0
		self.x = 0
		self.y = 0
		#Default direction
		self.direction = self.right
		#Level in which the character is located 
		self.labyrinth = labyrinth


	def move(self, direction):
		"""Method for moving the character"""
		
		#Move to the right
		if direction == 'right':
			#Not to exceed the screen
			if self.case_x < (NUMBER_SPITE_COT - 1):
				#We check that the destination box is not a wall
                # -tc- Ce n'est pas une bonne idée d'accéder à self.labyrinth.structure de cette manière.
                # -tc- Plutôt utiliser une méthode pour demander à labyrinth le contenu de case_y, case_x
				if self.labyrinth.structure[self.case_y][self.case_x+1] != 'm':
					#Moving a case
					self.case_x += 1
					#Calculation of the "real" position in pixels
                    # -tc- Définir self.x sous forme de property permet d'éviter d'avoir à mettre à jour
                    # -tc- case_x et x
					self.x = self.case_x * SIZE_SPRITE
			#Image in the right direction
			self.direction = self.right

		
		#Moving to the left
		if direction == 'left':
			if self.case_x > 0:
				if self.labyrinth.structure[self.case_y][self.case_x-1] != 'm':
					self.case_x -= 1
					self.x = self.case_x * SIZE_SPRITE
			self.direction = self.left
		
		#Moving to the up
		if direction == 'up':
			if self.case_y > 0:
				if self.labyrinth.structure[self.case_y-1][self.case_x] != 'm':
					self.case_y -= 1
					self.y = self.case_y * SIZE_SPRITE
			self.direction = self.up
		
		#Moving to the down
		if direction == 'down':
			if self.case_y < (NUMBER_SPITE_COT - 1):
				if self.labyrinth.structure[self.case_y+1][self.case_x] != 'm':
					self.case_y += 1
					self.y = self.case_y * SIZE_SPRITE
			self.direction = self.down


		#creact class Object
		#class Objects:
			# def init?	(self, item, ..):
			#charge image
			#def ether_position(self,window):
			#def needle_position(self,window):
			#def plastic-tube_position(self,window):
