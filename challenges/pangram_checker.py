import string

def is_pangram_with_sets(str1, alphabet=set(string.ascii_lowercase)):
	'''
	Checks to see if a given string is a pangram, i.e. contains every letter in the alphabet.
	'''

	#converts the string to lower case and then to a set.
	letter_set = set(str1.lower())
 	#Checks whether the alpha bet is a subset of letter_set (this allows for other characters aside from letters of the alphabet to appear in the string).
	return alphabet.issubset(letter_set)
