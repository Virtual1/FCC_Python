import unittest
import remainder_code

class RemainderTests(unittest.TestCase):
    def test_main(self):
        remainder = remainder_code.remainder
        self.assertIsInstance(remainder, int)
        self.assertEqual(remainder, 2)
