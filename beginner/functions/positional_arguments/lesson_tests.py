import unittest
from main import *

class PositionalArgumentsTests(unittest.TestCase):
    def test_main(self):
        self.assertIsNotNone(about_me)
        self.assertTrue(about_me)

    def test_correct_types(self):
        self.assertIsInstance(about_me, tuple)
        self.assertIsInstance(about_me[0], int)
        self.assertIsInstance(about_me[1], tuple)
        self.assertIsInstance(about_me[1][0], str)
        self.assertIsInstance(about_me[1][1], str)
