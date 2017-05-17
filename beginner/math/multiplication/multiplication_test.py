import unittest
import multiplication_code

class MultiplicationTests(unittest.TestCase):
    def test_main(self):
        product = multiplication_code.product
        self.assertIsInstance(product, int)
        self.assertEqual(product, 80)
