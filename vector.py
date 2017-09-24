import random

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def random(self, withinVector):
        return Vector(
            random.randrange(0, withinVector.x-1),
            random.randrange(0, withinVector.y-1),
        )

    @property
    def point(self):
        return (self.x, self.y)

    def __repr__(self):
        return '<Vector %s, %s>' % self.point

    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y)

    def __mul__(self, scalar):
        return Vector(self.x*scalar, self.y*scalar)

    __rmul__ = __mul__

    def __eq__(self, other):
        return self.point == other.point

    def __hash__(self):
        return hash(self.point)

    def within(self, other):
        return (
            self.x < other.x and self.y < other.y and 
            self.x > 0 and self.y > 0
        )