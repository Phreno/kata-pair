import unittest

from fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_1_doit_retourner_1(self):
        self.assertEqual(fizzbuzz(1), 1)

    def test_3_doit_retourner_fizz(self):
        self.assertEqual(fizzbuzz(3), "fizz")

    def test_6_doit_retourner_fizz(self):
        self.assertEqual(fizzbuzz(6), "fizz")

    def test_5_doit_retourner_buzz(self):
        self.assertEqual(fizzbuzz(5), "buzz")