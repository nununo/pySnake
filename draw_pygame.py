import pygame

from consts import Colors


class Drawer(object):

    def __init__(self, width, height, block_size):
        _, numfail = pygame.init()

        if numfail:
            raise RuntimeError("pygame.init failed")
    
        self.block_size = block_size
        self.surface = pygame.display.set_mode(
            (width * block_size, height * block_size)
        )


    def draw_background(self):
        self.surface.fill(Colors.BLACK)


    def draw_cell(self, x, y, color):

        pygame.draw.rect(
            self.surface,
            color,
            pygame.Rect(
                x * self.block_size,
                y * self.block_size,
                self.block_size,
                self.block_size,
            )
        )

    def flip_display(self):
        pygame.display.flip()
