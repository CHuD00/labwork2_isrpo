import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):
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
    def test_negative_area(self):
        with self.assertRaises(ValueError):
            area(-2)
    def test_string_area(self):
        with self.assertRaises(TypeError):
            area("1")

    def test_perimeter(self):
        res = perimeter(6)
        self.assertEqual(res, 24)
    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
    def test_float_perimeter(self):
        res = perimeter(3.4)
        self.assertEqual(res,  13.6)
    def test_negative_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(-7)
    def test_string_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter("i")