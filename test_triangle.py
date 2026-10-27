import unittest
from triangle import area, perimeter

class CircleTestCase(unittest.TestCase):
    def test_area(self):
        res = area(5, 6)
        self.assertEqual(res, 15)
    def test_zero_area(self):
        res = area(5, 0)
        self.assertEqual(res, 0)
    def test_float_area(self):
        res = area(3.6, 4)
        self.assertEqual(res,  7.2)

    def test_perimeter(self):
        res = perimeter(7, 5, 9)
        self.assertEqual(res, 21)
    def test_zero_perimeter(self):
        res = perimeter(0, 5, 14)
        self.assertEqual(res, 19)
    def test_float_perimeter(self):
        res = perimeter(2.2, 8.7, 1)
        self.assertEqual(res,  11.9)
    def test_right_triangle(self):
        res = perimeter(5, 5, 5)
        self.assertEqual(res, 15)