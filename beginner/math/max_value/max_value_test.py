import unittest
import max_value_code

class MaxValueTests(unittest.TestCase):
    def test_main(self):
        highest = max_value_code.highest 
        self.assertIsInstance(highest, int)
        self.assertEqual(highest, 9)
