import unittest
import sum_code

class SumTests(unittest.TestCase):
    def test_main(self):
        total = sum_code.total 
        self.assertIsInstance(total, int)
        self.assertEqual(total, 55)
