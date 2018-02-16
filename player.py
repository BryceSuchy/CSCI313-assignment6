import pygame
import random
import constants

class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """
 
    # -- Methods
    def __init__(self, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()

        self.images = []
        self.images.append(pygame.image.load("images/spaceship/u-spaceship1.png").convert_alpha())
        self.images.append(pygame.image.load("images/spaceship/u-spaceship2.png").convert_alpha())
        self.images.append(pygame.image.load("images/spaceship/u-spaceship3.png").convert_alpha())
        self.images.append(pygame.image.load("images/spaceship/u-spaceship4.png").convert_alpha())
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
 
    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y
 
    def update(self):
        """ Find a new position for the player"""
        if self.rect.x > 685:
            self.rect.x = self.rect.x - 1
        elif self.rect.y > 385:
            self.rect.y = self.rect.y - 1
        elif self.rect.x < 0:
            self.rect.x = self.rect.x + 1
        elif self.rect.y < 0:
            self.rect.y = self.rect.y + 1
        else:
            self.rect.x += self.change_x
            self.rect.y += self.change_y
            
        #iterates through the images, making it look animated
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
