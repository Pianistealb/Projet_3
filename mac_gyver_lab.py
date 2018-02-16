#! /usr/bin/env python3
# -*- coding: utf8 -*-

"""
Mac Gyver Labyrinth Game
Game in which we must move Mac Gyver in a labyrinth. 
He must retrieve three items to be able to exit the labyrinth and asleep 
the evil Murdoc to escape.
Python script
Files: mac_gyver_lab.py, classes.py, constantes.py, L1 + pictures + musics
"""

import pygame
from pygame.locals import *

from classes import *
from constantes import *

pygame.init()

#Open the window's pygame (square: width = height)
window = pygame.display.set_mode((WINDOW_SIDE, WINDOW_SIDE))
#Icon
icon = pygame.image.load(PICTURE_ICON)
pygame.display.set_icon(icon)
#Title
pygame.display.set_caption(TITLE_WINDOW)


#First loop
keep = 1
while keep:
	#loading and display from the home screen
	home = pygame.image.load(PICTURE_HOME).convert_alpha()
	window.blit(home, (0,0))

	#Refresh
	pygame.display.flip()

	#add music but: "don't stop me now" (for instant)
	pygame.mixer.music.load(MUSIC_HOME)
	pygame.mixer.music.play(-1)


	#These variables are reset to 1 at each loop turn
	continue_game = 1
	continue_home = 1
	finish_game = 1

	#Loop home
	while continue_home:
		#limitation speed for loop
		pygame.time.Clock().tick(30)

		for event in pygame.event.get():

			#if the user leaves, we put the varaibles loop to 0 to browse none and close
			if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
				continue_home = 0
				continue_game = 0
				finish_game = 0
				keep = 0
				#variable to load labyrinth
				continue_game = 0

			elif event.type == KEYDOWN and event.key == K_F1:				
				#Labyrinth launch
				continue_home = 0	#quitt home
				continue_game = 'L1'		#Labyrinth launch
				finish_game = 0




	if continue_game != 0:
		#display background
		background = pygame.image.load(PICTURE_BACKGROUND).convert()

		#Generate a labyrinth from the file
		labyrinth = Labyrinth(continue_game)
		labyrinth.generate()
		labyrinth.display(window)

		#Create characteres //METTRE LES IMAGES EN CONSTANTES
		mac_gyver = Character("pictures/Mac_Gyver_droite.png",
		"pictures/Mac_Gyver_gauche.png","pictures/Mac_Gyver_haut.png",
		"pictures/Mac_Gyver_bas.png", labyrinth)

		#Generat objects in labyrinth

		#object
		#display objects in labyrinth

	#Loop game
	while continue_game:
	
		#limitation speed for loop
		pygame.time.Clock().tick(30)
	
		for event in pygame.event.get():
		
			#If the player quitt, we put the variable for to continue game
			#And the principal variable at 0 for close the window
			if event.type == QUIT:
				continue_game = 0
				keep = 0
				finish_game = 0
		
			elif event.type == KEYDOWN:
				#If the player push escape return at the menu
				if event.key == K_ESCAPE:
					continue_game = 0
					
				#Touch for move Mac Gyver
				elif event.key == K_RIGHT:
					mac_gyver.move('right')
				elif event.key == K_LEFT:
					mac_gyver.move('left')
				elif event.key == K_UP:
					mac_gyver.move('up')
				elif event.key == K_DOWN:
					mac_gyver.move('down')			
			
		#Loadind the news positions
		window.blit(background, (0,0))
		labyrinth.display(window)
		window.blit(mac_gyver.direction, (mac_gyver.x, mac_gyver.y)) 
		#Macgyver.direction = picture in the good direction
		pygame.display.flip()

		#WIN -> Loop finish
		if labyrinth.structure[mac_gyver.case_y][mac_gyver.case_x] == 'a':
			finish_game = 1
			continue_game = 0
			continue_home = 0


	#Loop finish
	while finish_game:
		#loading and display from the finish screen
		finish = pygame.image.load(PICTURE_WIN).convert_alpha()
		window.blit(finish, (0,0))

		#Refresh

		pygame.display.flip()

		#add music but: "don't stop me now" (for instant)
		pygame.mixer.music.load(MUSIC_WIN)
		pygame.mixer.music.play(-1)


		#These variables are reset to 1 at each loop turn
		continue_game = 0
		continue_home = 0
		continue_finish = 1

		#Loop continue finish
		while continue_finish:
			#limitation speed for loop
			pygame.time.Clock().tick(30)

			for event in pygame.event.get():

				#if the user leaves, we put the varaibles loop to 0 to browse none and close
				if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
					continue_home = 0
					continue_game = 0
					continue_finish = 0
					keep = 0
					continue_game = 0
					finish_game =0

				elif event.type == KEYDOWN and event.key == K_RETURN:				
					#Menu home launch
					continue_home = 1
					continue_game = 0
					continue_finish = 0
					finish_game = 0
					#quitt home


	#Loop game over

					


