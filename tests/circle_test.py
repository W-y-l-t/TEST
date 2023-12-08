import unittest

import sys
sys.path.append(r"D:\a\TEST\TEST\methods")

from methods.circle import *
from resourсes.epsilon import *


class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        result = area(0)
        expected_result = 0
        self.assertEqual(expected_result, result)

    def test_small_data_area(self):
        result = area(239)
        expected_result = 179450.91396570255
        epsilon = get_epsilon(expected_result, result)
        self.assertGreaterEqual(1e-6, epsilon)

    def test_large_data_area(self):
        result = area(1234567890)
        expected_result = 4788283183070884321.4200489057006
        epsilon = get_epsilon(expected_result, result)
        self.assertGreaterEqual(1e-6, epsilon)

    def test_large_data_perimeter(self):
        result = perimeter(1234567890)
        expected_result = 7757018827.1637039278901849710357
        epsilon = get_epsilon(expected_result, result)
        self.assertGreaterEqual(1e-6, epsilon)

    def test_small_data_perimeter(self):
        result = perimeter(30)
        expected_result = 188.49555921538757
        epsilon = get_epsilon(expected_result, result)
        self.assertGreaterEqual(1e-6, epsilon)

    def test_zero_perimeter(self):
        result = perimeter(0)
        expected_result = 0
        self.assertEqual(expected_result, result)

    def test_wrong_data_perimeter_1(self):
        result = perimeter("1")
        expected_result = TypeError
        self.assertEqual(expected_result, result)

    def test_wrong_data_perimeter_2(self):
        result = perimeter(-1)
        expected_result = ArithmeticError
        self.assertEqual(expected_result, result)

    def test_wrong_data_area_1(self):
        result = area("1")
        expected_result = TypeError
        self.assertEqual(expected_result, result)

    def test_wrong_data_area_2(self):
        result = area(-1)
        expected_result = ArithmeticError
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
