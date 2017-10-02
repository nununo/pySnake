import pygame

from consts import Directions, Colors

class Snake(object):

    def __init__(self, game, color=Colors.GREEN):
        self.body = []
        self.game = game
        self.color = color
        self._is_alive = True
        self._just_ate = False
        self._come_to_life()
        self.direction = Directions.RIGHT
    
    @property
    def is_alive(self):
        return self._is_alive

    @property
    def head(self):
        return self.body[0]

    def die(self):
        self._is_alive = False

    def eat(self):
        self._just_ate = True

    def self_collide(self):
        return self.head in self.body[1:]

    def _come_to_life(self):
        self.body.append(self.game.random_vector())

    def turn(self, direction):
        if direction == Directions.OPPOSITE[self.direction]:
            self._is_alive = False
            return

        self.direction = direction

    def move(self):
        head_position = self.body[0] + Directions.DELTA_MOVEMENT[self.direction]
        self.body.insert(0, head_position)
        if not self._just_ate:
            self.body.pop()
        else:
            self._just_ate = False

    def draw(self):
        for block in self.body:
            pygame.draw.rect(
                self.game.surface,
                self.color,
                pygame.Rect(
                    *((block * self.game.block_size).point),
                    self.game.block_size, 
                    self.game.block_size
                ),
            )
