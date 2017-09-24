import pygame

from vector import Vector

# colors
class Colors:
    BLACK = pygame.Color(0, 0, 0)       # background
    GREEN = pygame.Color(0, 255, 0)     # snake
    RED = pygame.Color(255, 0, 0)       # game over title
    WHITE = pygame.Color(255, 255, 255) # score title
    BROWN = pygame.Color(165, 42, 42)       
    CHOCOLATE = pygame.Color(210, 105, 30)


#  initialize pygame surface / canvas
BLOCK_SIZE_PX = 10
WIDTH_BLOCKS = 72
HEIGHT_BLOCKS = 43
WIDTH_PX = WIDTH_BLOCKS * BLOCK_SIZE_PX
HEIGHT_PX = HEIGHT_BLOCKS * BLOCK_SIZE_PX


# snake movement constants
class Directions:
    UP = 'UP'
    DOWN = 'DOWN'
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'

    DIRECTIONS = [UP, RIGHT, DOWN, LEFT]

    OPPOSITE = {
        UP: DOWN,
        DOWN: UP,
        LEFT: RIGHT,
        RIGHT: LEFT,
    }

    DELTA_MOVEMENT = {
        UP: Vector(0,-1),
        RIGHT: Vector(1, 0),
        DOWN: Vector(0, 1),
        LEFT: Vector(-1, 0),
    }

# pygame event keys to movement
EVENT_KEY_DIRECTIONS = {
    pygame.K_UP: Directions.UP,
    pygame.K_DOWN: Directions.DOWN,
    pygame.K_LEFT: Directions.LEFT,
    pygame.K_RIGHT: Directions.RIGHT,
    ord('w'): Directions.UP,
    ord('s'): Directions.DOWN,
    ord('a'): Directions.LEFT,
    ord('d'): Directions.RIGHT,

}
