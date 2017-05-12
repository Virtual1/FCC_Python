import unittest
import square_root_code

class SquareRootTests(unittest.TestCase):
    def test_main(self):
        square_root = square_root_code.square_root 
        self.assertIsInstance(square_root, float)
        self.assertEqual(square_root, 9.0)
