from vector import Vector


class FakeGame(object):

    def __init__(self):
        # track draw calls
        self.draw_calls = []

    def random_vector(self):
        return Vector(10, 10)

    def draw_cell(self, x, y, color):
        self.draw_calls.append({
            'method': 'draw_cell',
            'args': (x, y, color),
        })
