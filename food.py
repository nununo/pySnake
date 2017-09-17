import pygame

class Food(object):

    def __init__(self, x, y, color):
        self.position = (x, y)
        self.color = color
    
    def draw(self, surface, block_size):
        pygame.draw.rect(
            surface, 
            self.color,
            pygame.Rect(*self.position, block_size, block_size),
        )