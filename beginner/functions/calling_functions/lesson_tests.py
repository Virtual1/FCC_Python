import unittest
import lesson_code

class CallingFunctionsTests(unittest.TestCase):
    def test_output(self):
        self.assertIsNotNone(lesson_code.result)
        self.assertIsInstance(lesson_code.result, str)
