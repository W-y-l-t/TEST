import unittest
import square


def get_epsilon(expected_result, result):
    return abs(expected_result - result) / max(1, abs(result))


class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        result = square.area(0)
        expected_result = 0
        self.assertEqual(expected_result, result)

    def test_small_data_area(self):
        result = square.area(239)
        expected_result = 57121
        self.assertEqual(expected_result, result)

    def test_large_data_area(self):
        result = square.area(9876543210)
        expected_result = 97546105778997104100
        self.assertEqual(expected_result, result)

    def test_float_area(self):
        result = square.area(0.5)
        expected_result = 0.25
        eps = get_epsilon(expected_result, result)
        self.assertGreaterEqual(1e-6, eps)

    def test_large_data_perimeter(self):
        result = square.perimeter(1234567890)
        expected_result = 4938271560
        self.assertEqual(expected_result, result)

    def test_small_data_perimeter(self):
        result = square.perimeter(1000)
        expected_result = 4000
        self.assertEqual(expected_result, result)

    def test_zero_perimeter(self):
        result = square.perimeter(0)
        expected_result = 0
        self.assertEqual(expected_result, result)

    def test_float_perimeter(self):
        result = square.perimeter(0.5)
        expected_result = 2.0
        eps = get_epsilon(expected_result, result)
        self.assertGreaterEqual(1e-6, eps)

    def test_wrong_data_perimeter_1(self):
        result = square.perimeter("1")
        expected_result = TypeError
        self.assertEqual(expected_result, result)

    def test_wrong_data_perimeter_2(self):
        result = square.perimeter(-1)
        expected_result = ArithmeticError
        self.assertEqual(expected_result, result)

    def test_wrong_data_area_1(self):
        result = square.area("1")
        expected_result = TypeError
        self.assertEqual(expected_result, result)

    def test_wrong_data_area_2(self):
        result = square.area(-1)
        expected_result = ArithmeticError
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
