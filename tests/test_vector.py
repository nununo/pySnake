import unittest

from vector import Vector


class VectorTests(unittest.TestCase):

    def setUp(self):
        self.v = Vector(4, 2)

    def tearDown(self):
        del self.v

    def test_point_property(self):
        point = self.v.point

        self.assertIsInstance(point, tuple)
        self.assertEqual(len(point), 2)

        x, y = point
        self.assertEqual(x, 4, "X property assertion")
        self.assertEqual(y, 2)

    def test_repr(self):
        r = repr(self.v)
        self.assertEqual(r, '<Vector 4, 2>')

    def test_add(self):
        result = self.v + self.v
        expected = Vector(8, 4)

        self.assertEqual(result, expected)
