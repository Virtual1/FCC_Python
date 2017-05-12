import unittest
import divmod_code

class DivmodTests(unittest.TestCase):
    def test_main(self):
        result = divmod_code.result 
        self.assertIsInstance(result, tuple)
        self.assertEqual(result, (3, 2))
