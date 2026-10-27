import unittest
from square import area, perimeter

class CircleTestCase(unittest.TestCase):
    def test_area(self):
        res = area(8)
        self.assertEqual(res, 64)
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)
    def test_float_area(self):
        res = area(4.7)
        self.assertEqual(res,  22.09)
    def test_unit(self):
        res = area(1)
        self.assertEqual(res, 1)

    def test_perimeter(self):
        res = perimeter(6)
        self.assertEqual(res, 24)
    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
    def test_float_perimeter(self):
        res = perimeter(3.4)
        self.assertEqual(res,  13.6)