import unittest

from methods import circle
from resourсes import epsilon


class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        result = circle.area(0)
        expected_result = 0
        self.assertEqual(expected_result, result)

    def test_small_data_area(self):
        result = circle.area(239)
        expected_result = 179450.91396570255
        eps = epsilon.get_epsilon(expected_result, result)
        self.assertGreaterEqual(1e-6, eps)

    def test_large_data_area(self):
        result = circle.area(1234567890)
        expected_result = 4788283183070884321.4200489057006
        eps = epsilon.get_epsilon(expected_result, result)
        self.assertGreaterEqual(1e-6, eps)

    def test_large_data_perimeter(self):
        result = circle.perimeter(1234567890)
        expected_result = 7757018827.1637039278901849710357
        eps = epsilon.get_epsilon(expected_result, result)
        self.assertGreaterEqual(1e-6, eps)

    def test_small_data_perimeter(self):
        result = circle.perimeter(30)
        expected_result = 188.49555921538757
        eps = epsilon.get_epsilon(expected_result, result)
        self.assertGreaterEqual(1e-6, eps)

    def test_zero_perimeter(self):
        result = circle.perimeter(0)
        expected_result = 0
        self.assertEqual(expected_result, result)

    def test_wrong_data_perimeter_1(self):
        result = circle.perimeter("1")
        expected_result = TypeError
        self.assertEqual(expected_result, result)

    def test_wrong_data_perimeter_2(self):
        result = circle.perimeter(-1)
        expected_result = ArithmeticError
        self.assertEqual(expected_result, result)

    def test_wrong_data_area_1(self):
        result = circle.area("1")
        expected_result = TypeError
        self.assertEqual(expected_result, result)

    def test_wrong_data_area_2(self):
        result = circle.area(-1)
        expected_result = ArithmeticError
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
