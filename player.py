import pygame
import random
import constants

from music import *
from art import *

class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """
 
    # -- Methods
    def __init__(self, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()

        self.images = []
        self.images.append(Art().get_image("spaceship/u-spaceship1.png"))
        self.images.append(Art().get_image("spaceship/u-spaceship2.png"))
        self.images.append(Art().get_image("spaceship/u-spaceship3.png"))
        self.images.append(Art().get_image("spaceship/u-spaceship4.png"))
        self.index = 0
        self.image = self.images[self.index]
 
        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(constants.BLUE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
        # -- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
        self.psuedocounter = 0
 
    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y
 
    def update(self):
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
        """ Find a new position for the player"""
        if self.rect.x > 685:
            MusicClass().play_once("boundary_sound")
            self.rect.x = self.rect.x - 1
        elif self.rect.y > 385:
            MusicClass().play_once("boundary_sound")
            self.rect.y = self.rect.y - 1
        elif self.rect.x < 0:
            MusicClass().play_once("boundary_sound")
            self.rect.x = self.rect.x + 1
        elif self.rect.y < 0:
            MusicClass().play_once("boundary_sound")
            self.rect.y = self.rect.y + 1
        else:
            self.rect.x += self.change_x
            self.rect.y += self.change_y
            
        #iterates through the images, making it look animated
        #self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
