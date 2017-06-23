import unittest
from main import *

class CallingFunctionsTests(unittest.TestCase):
    def test_output(self):
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
