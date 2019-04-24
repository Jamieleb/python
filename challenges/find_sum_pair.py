

def sum_pair(ls, target):

	'''
	Method to take an array and a number a return a pair from the array that sum to make the number. If no correct pair exists, returns false.
	Expects a list of numbers and a target number as arguments.

	'''
	while len(ls) > 0:
		x = ls.pop()
		y = target - x
		if y in ls:
			return (x, y)
	else:
		return False

