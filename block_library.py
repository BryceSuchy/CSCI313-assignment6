import pygame
import random
import constants

class Block(pygame.sprite.Sprite):
 
    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
 
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.change_x = 0
        self.change_y = 0

     #class method to have speed/position for block
    def changespeed(self, x, y):
        self.change_x = self.change_x + x
        self.change_y = self.change_y + y

    #update rectangle object with position/speed of block
    def update(self):
        self.rect.x = self.change_x + self.rect.x
        self.rect.y = self.change_y + self.rect.y 

        #boundry check, plays sound when colides at screen.
        if self.rect.x > 670:
            self.rect.x = 670
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > 390:
            self.rect.y = 390
