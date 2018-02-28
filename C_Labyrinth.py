"""
Class Labyrinth for Mac Gyver Labyrinth Game
Amandine Le Bras
"""

import pygame
from pygame.locals import *

from constantes import *
from C_Object import *
from C_Character import *


class Labyrinth:
	"""this class load the labyrinth"""

	def __init__(self, layout):
		"""in an instance"""
		self.layout = layout
		self.structure = 0

	def generate (self):
		"""Loading labyrinth with the file
		Creact a list principal, contene a list for line loading"""	
		#open file

		with open(self.layout, "r") as layout:
			structure_lab = []
			#we go through the letters contained in the file
			for line in layout:
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
		case_inventory = pygame.image.load(PICTURE_INVENTORY).convert_alpha()
		needle = pygame.image.load(PICTURE_NEEDLE).convert_alpha()
		tube = pygame.image.load(PICTURE_PLASTIC_TUBE).convert_alpha()
		ether = pygame.image.load(PICTURE_ETHER).convert_alpha()		
		num_line = 0
		for line in self.structure:
			#We go through the lists of lines
			num_case = 0
			for sprite in line:
				#The actual position in pixels is calculated
				x = num_case * SIZE_SPRITE
				y = num_line * SIZE_SPRITE
				if sprite in 'm':		   #m = Wall
					window.blit(wall, (x,y))
				elif sprite in 'd':		   #d = Start
					window.blit(wall_origine, (x,y))
				elif sprite in 'a':		   #a = Murdoc
					window.blit(murdoc, (x,y))
				elif sprite in 'i':			#i= inventory
					window.blit(case_inventory, (x,y))
				elif sprite in 'o1':		#01= needle
					window.blit(needle, (x, y))
				elif sprite in 'o2':		#02= plastic tube
					window.blit(tube, (x, y))
				elif sprite in 'o3':		#03= ether
					window.blit(ether, (x, y))
				elif sprite in 'i1':		#i1= needle in inventory
					window.blit(needle, (180, 0))
				elif sprite in 'i2':		#i2= plastic tube in inventory
					window.blit(tube, (270, 0))
				elif sprite in 'i3':		#i3= ether in inventory
					window.blit(ether, (360, 0))
				num_case += 1
			num_line += 1
