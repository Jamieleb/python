import math 

def is_prime(num):
	'''
	Checks if the number given as an argument is prime.

	'''

	#first checks that the number is not even, 1 or 0 (or negative).
	if num < 2 or num > 2 and not num % 2:
		return False

	#checks if all odd numbers up to the sqrt of num are a factor of num
	for x in range(3, int(math.sqrt(num))+1, 2):
		if not num % x:
			return False
	else:
		return True #if no numbers are a factor, returns True (that the number is prime)


def prime_counter(num):
	'''
	Function returns the number of primes that exist in the range up to and including the given number.
	'''
	count = 0
	
	for i in range(0,num+1):
		if is_prime(i):
			count += 1

	return count


