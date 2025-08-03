import unittest

from cal import add

class TestAdd (unittest.TestCase):
    def test_add_one(self):
        self.assertEqual(add(5,6), 11)

    def test_add_two(self):
        self.assertEqual(add(-5, 6), 1)