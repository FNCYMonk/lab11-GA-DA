# https://github.com/FNCYMonk/lab11-GA-DA
# Partner 1: Graham Avidano
# Partner 2: Daniel Atkins

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):  # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-2, -2), -4)
        self.assertEqual(add(1, -5), -4)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(subtract(1, 2), -1)
        self.assertEqual(subtract(-2, -2), 0)
        self.assertEqual(subtract(1, -5), 6)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(5, 4), 20)
        self.assertEqual(multiply(-2, 5), -10)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2, 10), 5)
        self.assertEqual(div(5, 20), 4)
        self.assertEqual(div(-2, 10), -5)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):  # 3 assertions
        self.assertAlmostEqual(logarithm(2,8),3)
        self.assertAlmostEqual(logarithm(5,1), 0)
        self.assertAlmostEqual(logarithm(5, 5), 1)

    def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
         with self.assertRaises(ValueError):
            logarithm(0, 5)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
        with self.assertRaises(ValueError):
            logarithm(5, 0)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(8, 15), 17)

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        with self.assertRaises(ValueError):
            square_root(-1)

        self.assertAlmostEqual(square_root(25), 5)
        self.assertAlmostEqual(square_root(16), 4)


##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()