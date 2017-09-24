import pygame

from consts import Directions, Colors

class Snake(object):

    def __init__(self, game, color=Colors.GREEN):
        self.body = []
        self.game = game
        self.color = color
        self.is_alive = True
        self._come_to_life()
        self.direction = Directions.RIGHT
    
    def _come_to_life(self):
        self.body.append(self.game.random_vector())

    def turn(self, direction):
        if direction == Directions.OPPOSITE[self.direction]:
            self.is_alive = False
            return

        self.direction = direction

    def move(self):
        head_position = self.body[0] + Directions.DELTA_MOVEMENT[self.direction]

        self.is_alive = self.game.within_limits(head_position)

        if not self.is_alive:
            return

        self.body.insert(0,head_position)

        if not self.game.is_food_here(head_position):
            self.body.pop()

    @property
    def head(self):
        return self.body[0]

    def draw(self):
        for block in self.body:
            pygame.draw.rect(
                self.game.surface,
                self.color,
                pygame.Rect(
                    *self.game.block_2_screen_position(block),
                    self.game.block_size, 
                    self.game.block_size
                ),
            )
