def is_prime(num):
	"""Checks if num is a positive prime number"""
	if num == 2:
		return 2
	elif num == 3:
		return 3
	elif num == 5:
		return 5
	elif num == 7:
		return 7
	elif type (num) == int:
		if num <= 1:
			return ("Negative input")
		for i in range(2,num):
			if num % i == 0:
				break
			elif num % 3 == 0:
				return False
			elif num % 5 == 0:
				return False
			elif num % 7 == 0:
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
print (list_of_prime_numbers (11))
print (list_of_prime_numbers (22))
print (list_of_prime_numbers (76))
print (list_of_prime_numbers (234))