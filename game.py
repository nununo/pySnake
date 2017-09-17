import time
import sys
import random

import pygame

from consts import Colors
from snake import Snake
from flora import Flora

class Game:

    def __init__(self, width=50, height=50, block_size=10):
        self.width = width
        self.height = height
        self.block_size = block_size
        self.score = 0

        self.init_pygame()

        self.snake = Snake(self)
        self.flora = Flora(self)

    def init_pygame(self):
        _, numfail = pygame.init()

        if numfail:
            raise RuntimeError("pygame.init failed")
    
        self.surface = pygame.display.set_mode(
            (self.width*self.block_size, self.height*self.block_size)
        )


    def run(self):
        # helps us set the pace
        fps_controller = pygame.time.Clock()  

        while True:
            self.snake.move()
            self.flora.draw()
            self.snake.draw()
            pygame.display.flip()
            fps_controller.tick(20)

            if not self.snake.is_alive:
                break

    def show_score(self, game_over=False):
        font = pygame.font.SysFont('Arial', 24)
        surface = font.render('Score: {}'.format(self.score), True, Colors.WHITE)

        rectangle = surface.get_rect()
        rectangle.midtop = (80, 10)

        self.surface.blit(surface, rectangle)

    def game_over():
        """ game over function
        """

        font = pygame.font.SysFont('Arial', 72)
        surface = font.render('Game over!', True, Colors.RED)
        rectangle = surface.get_rect()
        rectangle.midtop = (WIDTH_PX // 2, 15)

        surface.blit(surface, rectangle)

        self.show_score(surface)

        pygame.display.flip()
        time.sleep(2)

        pygame.quit()
        sys.exit()

    def random_position(self):
        return (
            random.randrange(0, self.width-1),
            random.randrange(0, self.height-1),
        )

    def within_limits(self, position):
        x, y = position
        return (x > 0 and x < self.width and y > 0 and y < self.height) 

    def is_food_here(self, position):
        return self.flora.is_food_here(position)

    def draw(self):
        self.flora.draw()
        self.snake.draw()
