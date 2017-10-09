import unittest

from snake import Snake
from consts import Directions
from .fake_game import FakeGame


class SnakeTests(unittest.TestCase):

    def setUp(self):
        self.snake = Snake(FakeGame())

    def test_initial_size_is_one(self):
        snake_length = len(self.snake)
        self.assertEqual(snake_length, 1)

    def test_initial_direction(self):
        self.assertEqual(self.snake.direction, Directions.RIGHT)

    def test_grow_by_one_after_eat_and_move(self):
        initial_length = len(self.snake)
        self.snake.eat()
        self.snake.move()
        final_length = len(self.snake)
        delta_length = final_length - initial_length
        self.assertEqual(delta_length, 1)
