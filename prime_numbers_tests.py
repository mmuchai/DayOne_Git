import unittest
from prime_numbers import list_of_prime_numbers, is_prime
''' Test Cases to check that a function with parameter n is a prime number.'''
class TestSolution (unittest.TestCase):
	def test_input_is_not_integer(self):
		self.assertEqual (is_prime("cats"), "Invalid")
	def test_input_is_not_negative(self):
		self.assertEqual (is_prime (-5), "Negative input")
	def test_input_is_two (self):
		self.assertEqual (is_prime (2), 2)
	def test_is_prime (self):
		self.assertEqual (is_prime(3), 3)
	def test_returns_list_of_primes(self):
		self.assertTrue(list_of_prime_numbers(10), [3,5,7])
	# def test_list_of_prime_numbers(self):
	# 	self.assertTrue (list_of_prime_numbers(10), [3, 5, 7])
	# def test_cannot_take_negative(self):
	# 	self.assertFalse(list_of_prime_numbers (-5), "Value should not be negative")
	# def test_must_be_integer(self):
	# 	self.assertTrue(list_of_prime_numbers ("cats"), "Can only take positive integer")
	# 	"""Fot string or boolean, raise and error"""
	# def test_list_prime_numbers_from_zero_to_n_inclusive(self):
	# 	self.assertTrue(list_of_prime_numbers (11), [3,5,7,11])
	# def test_should_not_be_below_two(self):
	# 	self.assertFalse (list_of_prime_numbers (1),)
	# def test_not_even_number(self):
	# 	self.assertFalse(list_of_prime_numbers (4))
if __name__ == '__main__':
	unittest.main()
