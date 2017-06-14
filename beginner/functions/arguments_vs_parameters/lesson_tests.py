import unittest
import lesson_code
from lesson_code import my_function

class ArgumentsVsParametersTests(unittest.TestCase):
    def test_output(self):
        self.assertIsNotNone(lesson_code.result)
        self.assertIsInstance(lesson_code.result, str)
        self.assertEqual(lesson_code.result, 'argument')

    def test_names_for_function_parameter_and_argument(self):
        f = open('lesson_code.py')
        lines = str(f.readlines())
        f.close()
        # The following tests only ensure that the named strings exist somewhere in the file, not that they are where they should be or have the correct values assigned.
        self.assertRegex(lines, 'my_function()', msg="The name of the function is incorrect.")
        self.assertRegex(lines, 'parameter', msg="The parameter must have the correct name.")
        self.assertRegex(lines, 'argument', msg="The argument must have the correct name.")
