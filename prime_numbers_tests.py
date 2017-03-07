import unittest
from prime_numbers import list_of_prime_numbers
''' Test Cases to check that a function with parameter n is a prime number.'''
class TestSolution (unittest.TestCase):
	def test_list_of_prime_numbers(self):
		self.assertEquals (list_of_prime_numbers(10), [3, 5, 7])
	def test_cannot_take_negative(self):
		self.assertFalse(list_of_prime_numbers (-5), "Value should not be negative")
	def test_must_be_integer(self):
		self.assertTrue(list_of_prime_numbers ("cats"), "Can only take positive integer")
		"""Fot string or boolean, raise and error"""
	def test_list_prime_numbers_from_zero_to_n_inclusive(self):
		self.assertEquals (list_of_prime_numbers (11), [3,5,7,11])
	def test_should_not_be_below_two(self):
		self.assertFalse (list_of_prime_numbers (1), False)
	def test_not_even_number(self):
		self.assertFalse(list_of_prime_numbers (4))
if __name__ == '__main__':
	unittest.main()
