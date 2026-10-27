import unittest
from rectangle import area, perimeter

class CircleTestCase(unittest.TestCase):
    def test_area(self):
        res = area(8, 4)
        self.assertEqual(res, 32)
    def test_zero_area(self):
        res = area(0, 5)
        self.assertEqual(res, 0)
    def test_float_area(self):
        res = area(2.5, 4.7)
        self.assertEqual(res,  11.75)
    def test_square(self):
        res = area(4, 4)
        self.assertEqual(res, 16)

    def test_perimeter(self):
        res = perimeter(8, 6)
        self.assertEqual(res, 28)
    def test_zero_perimeter(self):
        res = perimeter(0, 5)
        self.assertEqual(res, 10)
    def test_float_perimeter(self):
        res = perimeter(2.2, 8.7)
        self.assertEqual(res,  21.8)