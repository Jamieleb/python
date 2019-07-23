import math

def norm_prob(up_value, low_value, mean, stand_dev):
	var = stand_dev**2
	up_prob = (1/(math.sqrt(2*math.pi * var)))*math.e - ((up_value - mean)**2)/(2*var)
	low_prob = (1/(math.sqrt(2*math.pi * var)))*math.e - ((low_value - mean)**2)/(2*var)
	print(up_prob)
	print(low_prob)
	return up_prob - low_prob

def binom_calc(k, n, p):
	return (math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))*math.pow(p, k)*math.pow(1-p,n-k)

#upper_value, lower_value, mean, stand_dev = (input("Enter the upper value, lower value, mean, and standard deviation, separated by commas:\n").split(','))
result, num_trials, prob = (input("Enter the result, number of trails, and probability, separated by commas:\n").split(','))

#print(norm_prob(float(upper_value), float(lower_value), float(mean), float(stand_dev)))


print(binom_calc(float(result), float(num_trials), float(prob)))