import unittest

from fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_1_doit_retourner_1(self):
        self.assertEqual(fizzbuzz(1), 1)
