import unittest
from my_arithmetic_antonin_rouxel.pgcd import pgcd

class TestGCD(unittest.TestCase):
    def test_gcd_positive_numbers(self):
        self.assertEqual(pgcd(48, 18), 6)

    def test_gcd_with_zero(self):
        self.assertEqual(pgcd(0, 18), 18)
        self.assertEqual(pgcd(48, 0), 48)

    def test_gcd_same_numbers(self):
        self.assertEqual(pgcd(25, 25), 25)

    def test_gcd_one_and_number(self):
        self.assertEqual(pgcd(1, 18), 1)

    def test_gcd_negative_numbers(self):
        self.assertEqual(pgcd(-48, -18), -6)