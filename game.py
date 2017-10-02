import time
import sys

import pygame

from consts import Colors, Keyboard
from snake import Snake
from flora import Flora
from vector import Vector

class Game:

    def __init__(self, width=50, height=50, block_size=10):
        self.geometry = Vector(width, height)
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
            (self.geometry * self.block_size).point
        )

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # handle window close
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # make it the same as "window close"
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                elif event.key in Keyboard.DIRECTION_KEYS:
                    self.snake.turn(Keyboard.DIRECTION_KEYS[event.key])

    def process_collisions(self):
        if not self.within_limits(self.snake.head):
            self.snake.die()
            return

        if self.snake.self_collide():
            self.snake.die()
            return

        if self.flora.is_food_here(self.snake.head):
            self.snake.eat()
            self.flora.remove_food(self.snake.head)

    def run(self):
        # helps us set the pace
        fps_controller = pygame.time.Clock()  

        while True:
            self.handle_input()

            self.snake.move()
            self.process_collisions()

            self.draw()
            pygame.display.flip()
            fps_controller.tick(10)

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

    def random_vector(self):
        return Vector.random(self.geometry)

    def within_limits(self, xyVector):
        return xyVector.within(self.geometry)

    def _draw_background(self):
        self.surface.fill(Colors.BLACK)

    def draw(self):
        self._draw_background()
        self.flora.draw()
        self.snake.draw()
