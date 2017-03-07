def solution(n):
	"""A function that generates prime numbers from o to n, given a parameter n"""
	for num in range (2, n):
		result = []
		print (result)
		if isinstance (num, int):
			return True
		else:
			raise ValueError("Can only take positive integer")
			if num < 0:
				raise ValueError ("Should be non_negative")
			elif num < 2:
				return False
				''' n is not a prime number'''
			else:
			
				if n % num == 0:
					result.append(num)
					return False
					break
				else:
					return True