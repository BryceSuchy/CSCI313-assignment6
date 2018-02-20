import pygame
import constants

from level_manager import *
from game_screen import *
from music import *
from art import *

class CreditScreen():
    def __init__(self):
        pygame.mixer.quit()
        pygame.mixer.init()
        #Because this text never changes, we can load it in the constructor
        #Otherwise, we may need to move render into draw
        font = pygame.font.SysFont('Calibri', 25, True, False)
        self.image = Art().get_image("credit.png")
        #The underscore character indicates that this is a private instance variable
        #self._text = font.render("Otto's Game Template",True,constants.BLACK)
        MusicClass().play_repeat("creditmusic")

    def handle_keyboard_event(self, event):
        if event.type == pygame.KEYDOWN:
            # An argument can be made to place leaving the level in the main loop
            if event.key == pygame.K_ESCAPE:
                MusicClass().stop_repeat("creditmusic")
                pygame.mixer.quit()
                pygame.mixer.init()
                MusicClass().play_repeat("titlemusic")
                LevelManager().leave_level()
            else:
                pass

    #No need to do anything here, unless we've got some animation
    def update(self):
        pass
        
        
    def draw(self, screen):
        # Clear the screen
        screen.fill(constants.WHITE)
        screen.blit(self.image,[0,0])
        # Draw my title text!
        #screen.blit(self._text, [250, 250])

