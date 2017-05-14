import unittest
import assignment_code

class UnitTests(unittest.TestCase):
    def test_main(self):
        my_name = assignment_code.my_name
        self.assertIsInstance(my_name, str)
