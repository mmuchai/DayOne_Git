def is_prime(num):
	"""Checks if num is a positive prime number"""
	if num == 2:
		return 2
	if type (num) == int:
		if num <= 1:
			return ("Negative input")
		for i in range(2,num):
			if num % i == 0:
				break
			elif num % 3 == 0:
				return False
			else:
				return num
	else:
		return "Not prime"
	

def list_of_prime_numbers(n):
	"""A function that generates prime numbers from o to n, given a parameter n"""
	prime_numbers = []
	for num in range (2, n+1):
		
		#Checks if number can only have two factors, itself and one.
		prime_status = is_prime(n)
		invalids = ['Negative input', 'Not prime', False]
		if prime_status in invalids:
			return " Invalid tests"
		else:
			return [num for num in range (2, n+1) if is_prime(num)]
print (list_of_prime_numbers (119))