import unittest
from solution import solution
class TestSolution (unittest.TestCase):
	def test_addition (self):
		self.assertTrue (solution(10,20, "+"), 30)
	def test_subtraction (self):
		self.assertTrue (solution (20,10, "-"), 10)
	def test_division (self):
		self.assertTrue (solution (20,10, "/"), 2)
	def test_multiplication (self):
		self.assertTrue (solution (20,10, "*"), 200)
	def test_modulus(self):
		self.assertTrue (solution (4,3,"%"), 1 )
if __name__ == '__main__':
	unittest.main()


