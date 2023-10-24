import unittest

from methods.circle import *


class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        result = area(0)
        expected_result = 0
        self.assertEqual(expected_result, result)

    def test_small_data_area(self):
        result = area(239)
        expected_result = 179450.91396570255
        self.assertEqual(expected_result, result)

    def test_large_data_area(self):
        result = area(1234567890)
        expected_result = 4788283183070884321.4200489057006
        self.assertEqual(expected_result, result)

    def test_large_data_perimeter(self):
        result = perimeter(1234567890)
        expected_result = 7757018827.1637039278901849710357
        self.assertEqual(expected_result, result)

    def test_small_data_perimeter(self):
        result = perimeter(30)
        expected_result = 188.49555921538757
        self.assertEqual(expected_result, result)

    def test_zero_perimeter(self):
        result = perimeter(0)
        expected_result = 0
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()

