import block_library
import constants
import random
import pygame
import time

from art import *

class GoodBlock(block_library.Block):

    def __init__(self, color, width, height):
        #super.(GoodBlock, self)__init__()
        block_library.Block.__init__(self, color, width, height)
        
        self.velocity_x = random.randrange(-1, 2)
        self.velocity_y = random.randrange(-1, 2)
        self.color = color
        self.width = width
        self.height = height
        self.counter = 0
        self.images = []
        self.images.append(Art().get_image("goodbad/fuelcell1.png"))
        self.images.append(Art().get_image("goodbad/fuelcell2.png"))
        self.images.append(Art().get_image("goodbad/fuelcell3.png"))
        self.images.append(Art().get_image("goodbad/fuelcell4.png"))
        self.index = 0
        self.image = self.images[self.index]
        self.psuedocounter = 0
        

    def update(self):
        block_library.Block.update(self)
        ##this creates a fake-ish timer that just iterated the index every 15 frames
        self.psuedocounter += 1
        if self.psuedocounter is 15:
            self.index += 1
        elif self.psuedocounter is 30:
            self.index += 1
        elif self.psuedocounter is 45:
            self.index += 1
        elif self.psuedocounter is 60:
            self.index += 1
            self.psuedocounter = 0
        self.counter += 1
        if self.counter >= 60:  # Every 60 frames.
            self.counter = 0
            self.velocity_x = random.randrange(-1, 2)
            self.velocity_y = random.randrange(-1, 2)
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y
        #self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
