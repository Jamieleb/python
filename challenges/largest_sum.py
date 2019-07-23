'''
Given an array of numbers, calculate the largest sum of all possible blicks of consecutive elements within the array.
Numbers are a mix of positive and negative. If all values are positive, the answer will be the sum of the entire array.
'''

def largest_sum(ls):
	totals = []
	current_sum = 0

	for num in ls:
		if num >= 0:
			current_sum += num
		else:
			totals.append(current_sum)
			current_sum = 0

	return max(current_sum)


ls1 = [-1,-2,-3]
ls2 = []
ls3 = [1,2,3]
ls4 = [31,-41,59,26,-53,58,97,-93,-23,84]