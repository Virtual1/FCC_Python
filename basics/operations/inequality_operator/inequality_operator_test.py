import unittest
from inequality_operator_code import inequality

class InEqualityOperatorTests(unittest.TestCase):
    def test_main(self):
        self.assertIsNotNone(inequality(13))
        self.assertIsInstance(inequality(13), str)
        self.assertEqual(inequality(13), 'Equal to 13')
        self.assertNotEqual(inequality(13), 'Not Equal to 13')
