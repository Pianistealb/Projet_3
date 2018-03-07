
"""Class Item for Mac Gyver Labyrinth Game
Amandine Le Bras"""

import pygame
import random
from pygame.locals import *


class Item:
    def __init__(self, item, labyrinth):
        # load the Items image
        self.item = pygame.image.load(item).convert_alpha()
        self.labyrinth = labyrinth

    def position(self, window, representation):
        value_max = 1
        count = 0

        # until the maximum Items counter is reach (loop)
        while count < value_max:
            # We randomize the case_x position
            self.case_x = random.randint(0, 14)
            # same for case_y position
            self.tile_y = random.randint(0, 14)
            # if the randomized position is attribucted on a free space
            if self.labyrinth.structure[self.tile_y][self.case_x] == '0':
                # change the list's sprite with the Item's tag
                self.labyrinth.structure[self.tile_y][self.case_x] = representation
                # We define/accept the position for the Item
                count += 1
            # if the position is not free
            elif self.labyrinth.structure[self.tile_y][self.case_x] != '0':
                # nothing happen
                pass