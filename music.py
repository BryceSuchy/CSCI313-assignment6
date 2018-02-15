import pygame

class MusicClass():
    def play_once(strng_id):
        wave.open(strng_id,"r")
    def play_repeat(string_id):
        #pass in -1 for pygame.mixer.music.play() to repeat the music indefinitely
        pass
    def stop_repeat(string_id):
        pygame.mixer.music.stop()  
        pass
    def __init__():
        pygame.init()
