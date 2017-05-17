import unittest
import exponents_code

class ExponentsTests(unittest.TestCase):
    def test_main(self):
        power = exponents_code.power 
        self.assertIsInstance(power, int)
        self.assertEqual(power, 81)
