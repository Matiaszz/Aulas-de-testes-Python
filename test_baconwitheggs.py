'''
TDD -> Test driven development (desenvolvimento dirigido a testes);

Red
Step 1 -> Create the test and see the results;

Green
Step 2 -> Create the code and see passed test;

Refactor
Step 3 ->  Upgrade my code;

'''

import unittest
from baconwitheggs import bacon_with_eggs


class TestBaconWithEggs(unittest.TestCase):
    def test_baconwitheggs_should_be_returns_ASSERTIONERROR_if_doesnt_receive_an_integer_number(self):
        with self.assertRaises(AssertionError):
            bacon_with_eggs('')

    def test_baconwitheggs_should_be_returns_BACONWITHEGGS_if_the_number_is_multiple_of_3_and_5(self):

        inputs = (15, 30, 45, 60)
        output = 'BACON WITH EGGS'

        for ipt in inputs:
            with self.subTest(inputs=inputs, outputs=output):
                self.assertEqual(
                    bacon_with_eggs(ipt),
                    output,
                    msg=f'"{ipt}" is different of {output}')

    def test_baconwitheggs_should_be_returns_POOR_if_the_number_isnt_multiple_of_3_and_5(self):
        inputs = (1, 2, 4, 7, 8)
        output = 'POOR'

        for ipt in inputs:
            with self.subTest(inputs=inputs, outputs=output):
                self.assertEqual(
                    bacon_with_eggs(ipt),
                    output,
                    msg=f'"{ipt}" is different of {output}')

    def test_baconwitheggs_should_be_returns_BACON_if_the_number_is_multiple_only_of_3(self):
        inputs = (3, 6, 9, 12, 18, 21)
        output = 'BACON'

        for ipt in inputs:
            with self.subTest(inputs=inputs, outputs=output):
                self.assertEqual(
                    bacon_with_eggs(ipt),
                    output,
                    msg=f'"{ipt}" is different of {output}')

    def test_baconwitheggs_should_be_returns_EGGS_if_the_number_is_multiple_only_of_5(self):
        inputs = (5, 10, 20, 25, 35)
        output = 'EGGS'

        for ipt in inputs:
            with self.subTest(inputs=inputs, outputs=output):
                self.assertEqual(
                    bacon_with_eggs(ipt),
                    output,
                    msg=f'"{ipt}" is different of {output}')


unittest.main(verbosity=2)
