import unittest
from equality_operator_code import equality

class EqualityOperatorTests(unittest.TestCase):
    def test_main(self):
        value = equality.value
        self.assertEqual(equality(12), 'Equal')
