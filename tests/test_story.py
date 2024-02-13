import unittest
from story.core import Factors

class TestStory(unittest.TestCase):
    def test_factors_update(self):
        factors = Factors(2, 2, 2, 2)
        other = Factors(1, 0, -1, 2)
        factors.update(other)
        self.assertEqual(factors, Factors(3, 2, 1, 4))
        self.assertFalse(factors.any_failed())

    def test_a_zero_factor(self):
        factors = Factors(1, 1, 1, 0)
        self.assertTrue(factors.any_failed())

    def test_a_negative_factor(self):
        factors = Factors(1,-1, 1, 1)
        self.assertTrue(factors.any_failed())

if __name__ == '__main__':
    unittest.main()