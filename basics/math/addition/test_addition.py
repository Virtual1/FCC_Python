import unittest
import addition

class AdditionTests(unittest.TestCase):
    def test_main(self):
        total = addition.total
        self.assertIsInstance(total, int)
        self.assertEqual(total, 20)
