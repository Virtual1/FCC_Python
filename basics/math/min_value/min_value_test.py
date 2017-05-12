import unittest
import min_value_code

class MinValueTests(unittest.TestCase):
    def test_main(self):
        lowest = min_value_code.lowest
        self.assertIsInstance(lowest, int)
        self.assertEqual(lowest, 1)
