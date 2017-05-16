import unittest
from equality_operator_code import equality

class EqualityOperatorTests(unittest.TestCase):
    def test_main(self):
        self.assertIsNotNone(equality(12))
        self.assertIsInstance(equality(12), str)
        self.assertEqual(equality(12), 'Equal')
        self.assertIs(equality(12), 'Equal')
