import unittest

from methods.square import *
from resourсes.epsilon import *


class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        result = area(0)
        expected_result = 0
        self.assertEqual(expected_result, result)

    def test_small_data_area(self):
        result = area(239)
        expected_result = 57121
        self.assertEqual(expected_result, result)

    def test_large_data_area(self):
        result = area(9876543210)
        expected_result = 97546105778997104100
        self.assertEqual(expected_result, result)

    def test_float_area(self):
        result = area(0.5)
        expected_result = 0.25
        epsilon = get_epsilon(expected_result, result)
        self.assertGreaterEqual(1e-6, epsilon)

    def test_large_data_perimeter(self):
        result = perimeter(1234567890)
        expected_result = 4938271560
        self.assertEqual(expected_result, result)

    def test_small_data_perimeter(self):
        result = perimeter(1000)
        expected_result = 4000
        self.assertEqual(expected_result, result)

    def test_zero_perimeter(self):
        result = perimeter(0)
        expected_result = 0
        self.assertEqual(expected_result, result)

    def test_float_perimeter(self):
        result = perimeter(0.5)
        expected_result = 2.0
        epsilon = get_epsilon(expected_result, result)
        self.assertGreaterEqual(1e-6, epsilon)


if __name__ == '__main__':
    unittest.main()
