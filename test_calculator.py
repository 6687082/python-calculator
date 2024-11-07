import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)


    # Add the following test methods to the TestCalculator class:
    def test_add2(self):
        self.assertEqual(self.calc.add(20, -2), 18)
    # min
    def test_min(self):
        self.assertEqual(self.calc.subtract(3, 2), 1)  
    def test_min2(self):
        self.assertEqual(self.calc.subtract(10, 20), -10)
    # mul
    def test_mul(self):
        self.assertEqual(self.calc.multiply(-6, -2), 12)
    def test_mul2(self):
        self.assertEqual(self.calc.multiply(10, 2), 20)  
    # div
    def test_div(self):
        self.assertEqual(self.calc.divide(20, 10), 2)
    def test_div2(self):
        self.assertEqual(self.calc.divide(-20, 10), -2)
    # mod
    def test_mod(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)  
    def test_mod2(self):
        self.assertEqual(self.calc.modulo(3, 10), 3)

      

if __name__ == '__main__':
    unittest.main()