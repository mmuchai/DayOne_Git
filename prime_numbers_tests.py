import unittest
from prime_numbers import solution
''' Test Cases to check that a function with parameter n is a prime number.'''
class TestSolution (unittest.TestCase):
	def test_list_of_prime_numbers(self):
		self.assertTrue (solution(10), [3, 5, 7])
	def test_cannot_take_negative(self):
		self.assertFalse(solution (-5), ValueError(("Should be non_negative")))
	def test_must_be_integer(self):
		self.assertTrue(solution (5), [3,5])
		"""Fot string or boolean, raise and error"""
	def test_list_prime_numbers_from_zero_to_n_inclusive(self):
		self.assertTrue (solution (11), [3,5,7,11])
	def test_should_not_be_below_two(self):
		self.assertFalse (solution (1), False)
if __name__ == '__main__':
	unittest.main()
