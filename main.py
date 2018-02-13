"""

Josh, Callahan, Bryce

"""
import pygame
import random
import block_library
import constants
import goodblock_library
import badblock_library

class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """
 
    # -- Methods
    def __init__(self, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()
 
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
 
# Initialize Pygame
pygame.init()

img = pygame.image.load('images/RCAG.png')

font = pygame.font.SysFont('Calibri', 25, True, False)

# Set the title of the window
pygame.display.set_caption('REALLY COOL AWESOME GAME: LEVEL 1')
 
# Set the height and width of the screen
screen = pygame.display.set_mode([constants.screen_width, constants.screen_height])
 
# These are lists of 'good and bad sprites.' Each block in the program is
# added to these two different lists. The lists are managed by a class called 'Group.'
good_block_list = pygame.sprite.Group()
bad_block_list = pygame.sprite.Group()
 
# This is a list of every sprite. 
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
#goodblock = goodblock_library.GoodBlock(constants.GREEN, 20, 15)
# good sprites
for i in range(50):
    goodblock = goodblock_library.GoodBlock(constants.GREEN, 20, 15)
    goodblock.rect.x = random.randrange(constants.screen_width)
    goodblock.rect.y = random.randrange(constants.screen_height)
    # Add the block to the list of objects
    good_block_list.add(goodblock)
    all_sprites_list.add(goodblock)

    badblock = badblock_library.BadBlock(constants.RED, 20, 15)
    badblock.rect.x = random.randrange(constants.screen_width)
    badblock.rect.y = random.randrange(constants.screen_height)
    # Add the block to the list of objects
    bad_block_list.add(badblock)
    all_sprites_list.add(badblock)


# bad sprites
#for i in range(50):
    # This represents a block
    
 
    # Set a random location for the block
    #block.rect.x = random.randrange(constants.screen_width)
    #block.rect.y = random.randrange(constants.screen_height)
 
    # Add the block to the list of objects
    #bad_block_list.add(block)
    #all_sprites_list.add(block)
 
# Create a BLUE player block
player = Player(20, 15)
all_sprites_list.add(player)
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
        # Set the speed based on the key pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 3)
 
        # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -3)
    
    # This calls update on all the sprites
    #all_sprites_list.update()
       
    # Clear the screen
    screen.fill(constants.WHITE)
 
    # See if the player block has collided with anything.
    good_blocks_hit_list = pygame.sprite.spritecollide(player, good_block_list, True)
    bad_blocks_hit_list = pygame.sprite.spritecollide(player, bad_block_list, True)
 
    # Check the list of good collisions.
    for block in good_blocks_hit_list:
        score += 1
        print("Nice job man")

    # Check the list of good collisions.
    for block in bad_blocks_hit_list:
        score -= 1
        print("You are the worst player ever")

    text = font.render("Score: " + str(score), True, constants.BLACK)

    # Put the image of the text on the screen at 250x250
    screen.blit(text, [0, 0])
    screen.blit(img,(20,310))
    
    # Draw all the spites
    all_sprites_list.draw(screen)
    all_sprites_list.update()
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)
 
pygame.quit()
