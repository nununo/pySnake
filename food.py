import pygame

class Food(object):

    def __init__(self, xyVector, color):
        self.position = xyVector
        self.color = color
    
    def draw(self, game):
        pygame.draw.rect(
            game.surface, 
            self.color,
            pygame.Rect(
                *((self.position * game.block_size).point),
                game.block_size,
                game.block_size
            ),
        )
