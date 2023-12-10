import unittest
import triangle


def get_epsilon(expected_result, result):
    return abs(expected_result - result) / max(1, abs(result))


class TriangleTestCase(unittest.TestCase):
    def test_zero_area_1(self):
        result = triangle.area(15, 0)
        expected_result = 0
        self.assertEqual(expected_result, result)

    def test_zero_area_2(self):
        result = triangle.area(0, 15)
        expected_result = 0
        self.assertEqual(expected_result, result)

    def test_small_data_area(self):
        result = triangle.area(30, 239)
        expected_result = 3585
        self.assertEqual(expected_result, result)

    def test_large_data_area(self):
        result = triangle.area(11111111111, 9876543210)
        expected_result = 5.48696844994513031e+19
        eps = get_epsilon(expected_result, result)
        self.assertGreaterEqual(1e-6, eps)

    def test_large_data_perimeter(self):
        result = triangle.perimeter(1234567890, 9876543210, 5826873526534872)
        expected_result = 5826884637645972
        self.assertEqual(expected_result, result)

    def test_small_data_perimeter(self):
        result = triangle.perimeter(5, 432, 47)
        expected_result = 484
        self.assertEqual(expected_result, result)

    def test_float_perimeter(self):
        result = triangle.perimeter(0.5, 0.5, 0.5)
        expected_result = 1.5
        eps = get_epsilon(expected_result, result)
        self.assertGreaterEqual(1e-6, eps)

    def test_wrong_data_perimeter_1(self):
        result = triangle.perimeter("1", 1, "devTools!")
        expected_result = TypeError
        self.assertEqual(expected_result, result)

    def test_wrong_data_perimeter_2(self):
        result = triangle.perimeter(-1, -0.5, 120921)
        expected_result = ArithmeticError
        self.assertEqual(expected_result, result)

    def test_wrong_data_area_1(self):
        result = triangle.area("1", 121212)
        expected_result = TypeError
        self.assertEqual(expected_result, result)

    def test_wrong_data_area_2(self):
        result = triangle.area(-1, -13983)
        expected_result = ArithmeticError
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
