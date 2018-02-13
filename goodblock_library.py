import block_library
import constants
import random

class GoodBlock(block_library.Block):

    def __init__(self, color, width, height):
        #super.(GoodBlock, self)__init__()
        block_library.Block.__init__(self, color, width, height)

        self.velocity_x = random.randrange(-1, 2)
        self.velocity_y = random.randrange(-1, 2)
        self.color = color
        self.width = width
        self.height = height
        self.counter = 0

    def update(self):
        block_library.Block.update(self)
        self.counter += 1
        if self.counter >= 60:  # Every 60 frames.
            self.counter = 0
            self.velocity_x = random.randrange(-1, 2)
            self.velocity_y = random.randrange(-1, 2)
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y
