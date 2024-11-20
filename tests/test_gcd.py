import unittest
from src.my_arithmetic_antonin_rouxel.gcd import gcd

class TestGCD(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(100, 10), 10)
        self.assertEqual(gcd(7, 3), 1)
        self.assertEqual(gcd(20, 8), 4)
