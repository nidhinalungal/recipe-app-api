"""
Sample tests
"""
from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        # Test adding numbers together
        res = calc.add(5,6)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        # Test subtracting numbers
        res = calc.subtract(10,15)

        self.assertEqual(res, 5)

    def test_multiply_numbers(self):
        # Test multiplying numbers
        res = calc.multiply(10,15)

        self.assertEqual(res, 150)

    def test_devide_numbers(self):
        # Test multiplying numbers
        res = calc.devide(150,3)

        self.assertEqual(res, 50)