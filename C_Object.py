"""
Class Object for Mac Gyver Labyrinth Game
Amandine Le Bras
"""

import pygame
import random
from pygame.locals import *

# -tc-from character import Character (ici renommer C_Character.py en character.py)
# -tc- from labyrinth import Labyrinth
from constantes import *
from C_Character import *
from C_Labyrinth import *


class Object:
	def __init__(self, object, labyrinth):
		# load the objects image
		self.object = pygame.image.load(object).convert_alpha()
		self.labyrinth = labyrinth

    # -tc- Pourquoi créer trois méthodes position1(), position2(), et position3() est nécessaire
    # -tc- alors que une seule méthodes position() est nécessaire. La méthode ci-dessous est
    # -tc- simplement à appeler 3 fois avec le paramètre reprensentation égal à 'o1', 'o2' et 'o3'
	def position(self, window, representation):
		value_max = 1
		count = 0

		# until the maximum objects counter is reach (loop)
		while count < value_max:
			# We randomize the case_x position
			self.case_x = random.randint(0, 14)
			# same for case_y position
			self.tile_y = random.randint(0, 14)
			# if the randomized position is attribucted on a free space
			if self.labyrinth.structure[self.tile_y][self.case_x] == '0':
				# change the list's sprite with the object's tag
				self.labyrinth.structure[self.tile_y][self.case_x] = representation
				# We define/accept the position for the object
				count += 1
			# if the position is not free
			elif self.labyrinth.structure[self.tile_y][self.case_x] != '0':
				# nothing happen
				pass

    # -tc- Avec la méthode position ci-dessus, plus besoin d'utiliser
    # -tc- les trois méthodes ci-dessous dont le code est répété 3x.
	def position1(self, window):
		value_max = 1
		count = 0

		# until the maximum objects counter is reach (loop)
		while count < value_max:
			# We randomize the case_x position
			self.case_x = random.randint(0, 14)
			# same for case_y position
			self.tile_y = random.randint(0, 14)
			# if the randomized position is attribucted on a free space
			if self.labyrinth.structure[self.tile_y][self.case_x] == '0':
				# change the list's sprite with the object's tag
				self.labyrinth.structure[self.tile_y][self.case_x] = 'o1'
				# We define/accept the position for the object
				count += 1
			# if the position is not free
			elif self.labyrinth.structure[self.tile_y][self.case_x] != '0':
				# nothing happen
				pass

	def position2(self, window):

		value_max = 1
		count = 0
		while count < value_max:
			self.case_x = random.randint(0, 14)
			self.tile_y = random.randint(0, 14)
			if self.labyrinth.structure[self.tile_y][self.case_x] == '0':
				self.labyrinth.structure[self.tile_y][self.case_x] = 'o2'
				count += 1
			elif self.labyrinth.structure[self.tile_y][self.case_x] != '0':
				pass	

	def position3(self, window):
		value_max = 1
		count = 0
		while count < value_max:
			self.case_x = random.randint(0, 14)
			self.tile_y = random.randint(0, 14)
			if self.labyrinth.structure[self.tile_y][self.case_x] == '0':
				self.labyrinth.structure[self.tile_y][self.case_x] = 'o3'
				count += 1
			elif self.labyrinth.structure[self.tile_y][self.case_x] != '0':
				pass
