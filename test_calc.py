import unittest
import calc
class TestCalc(unittest.TestCase):
    # Inheriting from unittest.TestCase gives us access to a lot of
    # different testing capabilities within that class

    """In order to put a cursor in a few lines at the same time we press alt + cursor in a needed place"""
    """We always name our functions starting with 'test_' in other hand it won`t work"""
    def test_add(self):
        # result = calc.add(10, 5)
        # self.assertEqual(result, 15)
        self.assertEqual(calc.add(1, 4), 5)
        # we make a few more edge cases, to test more examples
        self.assertEqual(calc.add(6, -2), 4)
        self.assertEqual(calc.add(-6, -4), -10)
        self.assertEqual(calc.add(13, -23), -10)

    def test_subtraction(self):
        self.assertEqual(calc.subtraction(5, 3), 2)
        self.assertEqual(calc.subtraction(6, -2), 8)
        self.assertEqual(calc.subtraction(-6, -4), -2)
        self.assertEqual(calc.subtraction(13, -23), 36)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 2), 20)
        self.assertEqual(calc.multiply(6, -2), -12)
        self.assertEqual(calc.multiply(-6, -4), 24)
        self.assertEqual(calc.multiply(13, 0), 0)

    def test_division(self):
        self.assertEqual(calc.divide(10, 2), 5)
        self.assertEqual(calc.divide(6, -2), -3)
        self.assertEqual(calc.divide(-6, -4), 1.5)
        # to catch an error such as a division by 0 we do:
        # self.assertRaises(ValueError, calc.divide, 10, 0)
        # How to call function normally instead of passing it arguments. We can do it if we test the exceptions using
        # context manager. That will allow us check and test the exceptions properly
        with self.assertRaises(ValueError):
            calc.divide(10, 0)

"""It would be nice if we could run our test by passing only -
    'python test_calc.py', without specifying 'python -m unittest test_calc.py' 
    It also allows us to run this test directly from our editor. To do this
    we write next two lines"""

if __name__ == "__main__": # if we run this code directly we run the code within our conditional
    unittest.main()

