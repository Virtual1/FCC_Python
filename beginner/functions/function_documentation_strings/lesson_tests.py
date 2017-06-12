import unittest
from lesson_code import docstring_function

class FunctionDocumentationStringsTests(unittest.TestCase):
    def test_main(self):
        self.assertIsNone(docstring_function())
        self.assertIsNotNone(docstring_function.__doc__)
        self.assertIsInstance(docstring_function.__doc__, str)
