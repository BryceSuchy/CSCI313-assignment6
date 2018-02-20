import pygame

class MusicClass():
    def __init__(self):
        pygame.mixer.init()
        self._fuelsound = pygame.mixer.Sound("sounds/fuelSound.wav")
        self._astroidsound = pygame.mixer.Sound("sounds/astroidSound.wav")
        self._deathsound = pygame.mixer.Sound("sounds/deathSound.wav")
        self._titlemusic = pygame.mixer.Sound("sounds/titleScreenMusic.wav")
        self._gamemusic = pygame.mixer.Sound("sounds/gameMusic.wav")
        self._creditmusic = pygame.mixer.Sound("sounds/creditScreenMusic.wav")
    def play_once(self, soundstring):
        if (soundstring == "fuelsound"):
            self._fuelsound.play()
        elif (soundstring == "astroidsound"):
            self._astroidsound.play()
        elif (soundstring == "deathsound"):
            self._deathsound.play()
        elif (soundstring == "titlemusic"):
            self._titlemusic.play()
        elif (soundstring == "gamemusic"):
            self._gamemusic.play()
        elif (soundstring == "creditmusic"):
            self._creditmusic.play()
        else:
            print("That's not a valid identifier")
        pass
    def play_repeat(self, soundstring):
        #pass in -1 for pygame.mixer.music.play() to repeat the music indefinitely
        if (soundstring == "titlemusic"):
            self._titlemusic.play(-1)
        elif (soundstring == "gamemusic"):
            self._gamemusic.play(-1)
        elif (soundstring == "creditmusic"):
            self._creditmusic.play(-1)
        else:
            print("That's not a valid identifier")
        pass
    def stop_repeat(self, soundstring):
        if (soundstring == "titlemusic"):
            self._titlemusic.stop()
        elif (soundstring == "gamemusic"):
            self._gamemusic.stop()
        elif (soundstring == "creditmusic"):
            self._creditmusic.stop()
        else:
            print("That's not a valid identifier")  
        pass
    
