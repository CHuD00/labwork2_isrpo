import unittest
import math
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    def test_area(self):
        res = area(8)
        self.assertEqual(res, math.pi * 64)
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)
    def test_float_area(self):
        res = area(2.5)
        self.assertEqual(res, math.pi * 6.25)

    def test_perimeter(self):
        res = perimeter(8)
        self.assertEqual(res, math.pi * 16)
    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
    def test_float_perimeter(self):
        res = perimeter(2.2)
        self.assertEqual(res, math.pi * 4.4)