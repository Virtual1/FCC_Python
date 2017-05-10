import unittest
import addition

class AdditionTests(unittest.TestCase):
    def test_main(self):
        total = addition.total
        self.assertIsInstance(total, int)
        self.assertEqual(total, 20)

# To run the tests from the console:
# Make sure that you are in the 'addition' directory
# ⇒  python3 -m unittest test_addition
