try:
    import sys
    from pathlib import Path

    src_path = Path(__file__).parent.parent / 'src'
    sys.path.append(str(src_path))

except Exception:
    raise

import unittest
from calculator import sums, sub  # type: ignore


class TestCalculator(unittest.TestCase):
    # the names of functions are verbose
    # self.assertCONDITION(executedFunction(), expectedReturn)

    total_errors = 0

    # ---------------------------SUM TESTS----------------------------------
    def test_sum_5_and_5_returns_0(self):
        self.assertEqual(sums(5, 5), 10)

    def test_sum_with_many_inputs(self):
        x_y_outputs = [
            (10, 10, 20),
            (15, 15, 30),
            (90, 90, 180),

        ]

        for x_y_out in x_y_outputs:
            with self.subTest(x_y_out=x_y_out):

                x, y, output = x_y_out

                self.assertEqual(sums(x, y), output)

    def test_sum_parameter_x_isnt_int_or_float_should_be_returns_error(self):
        with self.assertRaises(AssertionError):
            sums('a', 2)

    def test_sum_parameter_y_isnt_int_or_float_should_be_returns_error(self):
        with self.assertRaises(AssertionError):
            sums('a', '2')

    # --------------------- SUBS TESTS --------------------------------------

    def test_sub_5_and_5_returns_0(self):
        self.assertEqual(sub(5, 5), 0)

    def test_sub_with_many_inputs(self):
        x_y_outputs = [
            (10, 10, 0),
            (15, 15, 0),
            (90, 90, 0),

        ]

        for x_y_out in x_y_outputs:
            with self.subTest(x_y_out=x_y_out):
                x, y, output = x_y_out

                self.assertEqual(sub(x, y), output)

    def test_sub_parameter_x_isnt_int_or_float_should_be_returns_error(self):
        with self.assertRaises(AssertionError):
            sub('a', 2)

    def test_sub_parameter_y_isnt_int_or_float_should_be_returns_error(self):
        with self.assertRaises(AssertionError):
            sub('a', 'asdfa')


if __name__ == '__main__':
    unittest.main(verbosity=2)
