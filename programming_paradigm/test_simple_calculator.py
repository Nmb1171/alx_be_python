import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):

        self.calc = SimpleCalculator()

    def test_addition(self):
        """ Test the Substraction method. """
        self.assertEqual(self.calc.subtract(10, 5), 5)