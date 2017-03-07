def is_prime(num):
	"""Checks if num is prime"""
	if num isPrime:
		return num
	return False

def list_of_primes(n):
	primes = []
	for num in range(2,n):
		if is_prime(num):
			primes.append(num)


def list_of_prime_numbers(n):
	"""A function that generates prime numbers from o to n, given a parameter n"""
	for num in range (2, n):
		result = []
		#Checks if number can only have two factors, itself and one.
		if n % num == 0:
			continue
		else:

			result.append(num)
			return result
		if isinstance (num, int):
			return True
		else:
			print ("Can only take positive integer")
			if num < 0:
				print ("Value should not be negative")
			elif num < 2:
				return False
			elif (num % 2 == 0):
				return False
			