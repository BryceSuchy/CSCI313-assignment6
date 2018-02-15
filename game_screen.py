import pygame
import random
import block_library
import constants
import goodblock_library
import badblock_library
import player

from level_manager import *
from screen import *

class GameScreen(Screen):
    def __init__(self):
        self._score = 0
        self._font = pygame.font.SysFont('Calibri', 25, True, False)
        # added to these two different lists. The lists are managed by a class called 'Group.'
        self._good_block_list = pygame.sprite.Group()
        self._bad_block_list = pygame.sprite.Group()
        self._all_sprites_list = pygame.sprite.Group()
        
        # Create a BLUE player block
        self._player1 = player.Player(20, 15)
        self._all_sprites_list.add(self._player1)
        
        #goodblock = goodblock_library.GoodBlock(constants.GREEN, 20, 15)
        # good sprites
        for i in range(50):
            goodblock = goodblock_library.GoodBlock(constants.GREEN, 20, 15)
            goodblock.rect.x = random.randrange(constants.SCREEN_WIDTH)
            goodblock.rect.y = random.randrange(constants.SCREEN_HEIGHT)
            # Add the block to the list of objects
            self._good_block_list.add(goodblock)
            self._all_sprites_list.add(goodblock)

            badblock = badblock_library.BadBlock(constants.RED, 20, 15)
            badblock.rect.x = random.randrange(constants.SCREEN_WIDTH)
            badblock.rect.y = random.randrange(constants.SCREEN_HEIGHT)
            # Add the block to the list of objects
            self._bad_block_list.add(badblock)
            self._all_sprites_list.add(badblock)



    def handle_keyboard_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                LevelManager().leave_level()
            # Set the speed based on the key pressed
            elif event.key == pygame.K_LEFT:
                self._player1.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                self._player1.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                self._player1.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                self._player1.changespeed(0, 3)
 
        # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self._player1.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                self._player1.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                self._player1.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                self._player1.changespeed(0, -3)
                
    def update(self):
        # See if the player block has collided with anything.
        self._good_blocks_hit_list = pygame.sprite.spritecollide(self._player1, self._good_block_list, True)
        self._bad_blocks_hit_list = pygame.sprite.spritecollide(self._player1, self._bad_block_list, True)
 
        # Check the list of good collisions.
        for block in self._good_blocks_hit_list:
            self._score += 1
            print("Nice job man")

        # Check the list of good collisions.
        for block in self._bad_blocks_hit_list:
            self._score -= 1
            print("You are the worst player ever")



    def draw(self, screen):
        # Clear the screen
        screen.fill(constants.WHITE)
        self._text = self._font.render("Score: " + str(self._score), True, constants.BLACK)
        screen.blit(self._text, [0, 0])
        self._all_sprites_list.draw(screen)
        self._all_sprites_list.update()
