import pygame

class Art():
    def __init__(self):
        #self._astroid = "images/goodbad/astroid.png"
        self._astroid = pygame.image.load("images/goodbad/astroid.png").convert_alpha()
        self._player1 = "images/spaceship/u-spaceship1.png"
        self._player2 = "images/spaceship/u-spaceship2.png"
        self._player3 = "images/spaceship/u-spaceship3.png"
        self._player4 = "images/spaceship/u-spaceship4.png"
        self._fuel1 = "images/goodbad/FuelCell1.png"
        self._fuel2 = "images/goodbad/FuelCell2.png"
        self._fuel3 = "images/goodbad/FuelCell3.png"
        self._fuel4 = "images/goodbad/FuelCell4.png"
        #self._background = "images/background.png"
        self._background = pygame.image.load("images/background.png").convert()
        #self._title = "images/title.png"
        self._title = pygame.image.load("images/title.png").convert()
    def get_image(self, name):
        #pygame.image.load(name).convert_alpha()
        if(name ==  "title"):
            return self._title
        '''
        #if(name == "astroid"):
            #pygame.image.load(self._astroid).convert_alpha()
        if(name == "astroid"):
            self._astroid
        elif(name == "player1"):
            pygame.image.load(self._player1).convert_alpha()
        elif(name == "player2"):
            pygame.image.load(self._player2).convert_alpha()
        elif(name == "player3"):
            pygame.image.load(self._player3).convert_alpha()
        elif(name == "player4"):
            pygame.image.load(self._player4).convert_alpha()
        elif(name == "fuel1"):
            pygame.image.load(self._fuel1).convert_alpha()
        elif(name == "fuel2"):
            pygame.image.load(self._fuel2).convert_alpha()
        elif(name == "fuel3"):
            pygame.image.load(self._fuel3).convert_alpha()
        elif(name == "fuel4"):
            pygame.image.load(self._fuel4).convert_alpha()
       # elif(name == "background"):
          #  pygame.image.load(self._background).convert()
        elif(name == "background"):
            self._background
        #elif(name == "title"):
            #pygame.image.load(self._title).convert()
        elif(name == "title"):
            self._title
            #pygame.image.load("images/title.png").convert()
            print("you got here")
        else:
            print("That is not a valid identifier")
        '''
        pass
    #def load_img(self, screen):
        
            

