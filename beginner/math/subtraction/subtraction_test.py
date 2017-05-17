import unittest
import subtraction_code

class SubtractionTests(unittest.TestCase):
    def test_main(self):
        total = subtraction_code.total
        self.assertIsInstance(total, int)
        self.assertEqual(total, 10)

# To run the tests from the console:
# Make sure that you are in the 'subtraction' directory
# ⇒  python3 -m unittest test_subtraction
