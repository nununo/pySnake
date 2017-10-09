import unittest

from food import Food
from vector import Vector
from consts import Colors
from .fake_game import FakeGame


class FoodTests(unittest.TestCase):

    def setUp(self):
        self.food = Food(Vector(0, 0), Colors.CHOCOLATE)

    def tearDown(self):
        del self.food

    def test_instantiation(self):
        self.assertEqual(self.food.color, Colors.CHOCOLATE)
        self.assertEqual(self.food.position, Vector(0, 0))

    def test_draw(self):
        game = FakeGame()
        self.food.draw(game)

        num_draw_calls = len(game.draw_calls)
        self.assertEqual(num_draw_calls, 1, 'Number of draw calls!')

        draw_call = game.draw_calls[0]
        self.assertEqual(draw_call['method'], 'draw_cell')

        draw_call_args = draw_call['args']
        self.assertEqual(draw_call_args, (0, 0, Colors.CHOCOLATE))
