import random

from food import Food
from consts import Colors

class Flora(object):

    def __init__(self, game, food_count=5):
        self.food_list = {}
        self.game = game
        self.generate_food(food_count)

    def generate_food(self, quantity=1):
        for _ in range(quantity):
            food = Food(*self.game.random_position(), self._random_color())
            self.food_list[food.position] = food

    def remove_food(self, position):
        food = self.food_list.get(position)
        if food != None:
            del self.food_list[food.position]
        return food

    def is_food_here(self, position):
        return position in self.food_list

    def draw(self):
        for food in self.food_list.values():
            food.draw(self.game.surface, self.game.block_size)

    def _random_color(self):
        return random.choice([Colors.BROWN, Colors.CHOCOLATE])
