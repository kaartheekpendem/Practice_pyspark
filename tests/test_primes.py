import unittest
from unittest.mock import MagicMock
from src.primenumbers import primenums
class test_prime(unittest.TestCase):
    def test_valid_prime(self):
        a= 10
        result = primenums(a)
        self.assertEqual([3,5,7,9], result)

    def test_invalid_prime(self):
        a=4
        result = primenums(a)
        self.assertEqual([3],result)
