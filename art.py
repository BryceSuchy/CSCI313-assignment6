import pygame

class Art():
    def __init__(self):
        pass
    def get_image(self, file_name):
        return pygame.image.load("images/" + file_name)
        
        
            

