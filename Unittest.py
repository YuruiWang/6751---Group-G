import Incarnation_ONE
import unittest
import math


class TestMathFunctions(unittest.TestCase):

    def test_sin(self):
        # Test sin function against math.sin for various values of x
        self.assertAlmostEqual(Incarnation_ONE.calculating_sine(0), math.sin(0))
        self.assertAlmostEqual(Incarnation_ONE.calculating_sine(math.pi/2), math.sin(math.pi/2))
        self.assertAlmostEqual(Incarnation_ONE.calculating_sine(math.pi), math.sin(math.pi))

    def test_cos(self):
        # Test cos function against math.cos for various values of x
        self.assertAlmostEqual(Incarnation_ONE.calculating_cosine(0), math.cos(0))
        self.assertAlmostEqual(Incarnation_ONE.calculating_cosine(math.pi/2), math.cos(math.pi/2))
        self.assertAlmostEqual(Incarnation_ONE.calculating_cosine(math.pi), math.cos(math.pi))

    def test_value_of_pi(self):
        # Test calculating_pi function against math.pi for various number of terms
        self.assertAlmostEqual(Incarnation_ONE.calculating_pi(1000), math.pi, places=2)

    def test_factorial(self):
        # Test caluclating_factorial function for various values of n
        self.assertEqual(Incarnation_ONE.caluclating_factorial(0), 1)
        self.assertEqual(Incarnation_ONE.caluclating_factorial(1), 1)
        self.assertEqual(Incarnation_ONE.caluclating_factorial(5), 120)

if __name__ == '__main__':
    unittest.main()