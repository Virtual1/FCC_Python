import unittest
import assignment_operator_code

class AssignmentOperatorTests(unittest.TestCase):
    def test_main(self):
        my_name = assignment_operator_code.my_name
        self.assertIsNotNone(my_name)
        self.assertIsInstance(my_name, str)
