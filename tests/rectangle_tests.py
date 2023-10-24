import unittest

from methods.rectangle import *


class RectangleTestCase(unittest.TestCase):
    def test_zero_area_1(self):
        result = area(15, 0)
        expected_result = 0
        self.assertEqual(expected_result, result)

    def test_zero_area_2(self):
        result = area(0, 15)
        expected_result = 0
        self.assertEqual(expected_result, result)

    def test_square_area(self):
        result = area(239, 239)
        expected_result = 57121
        self.assertEqual(expected_result, result)

    def test_large_data_area(self):
        result = area(1234567890, 9876543210)
        expected_result = 12193263111263526900
        self.assertEqual(expected_result, result)

    def test_large_data_perimeter(self):
        result = perimeter(1234567890, 9876543210)
        expected_result = 22222222200
        self.assertEqual(expected_result, result)

    def test_square_perimeter(self):
        result = perimeter(1000, 1000)
        expected_result = 4000
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
