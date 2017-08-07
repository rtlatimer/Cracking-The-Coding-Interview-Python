'''
1.4 Palindrome Permutation:
Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards.
A permutation is a rearrangement of letters. The palindrome does not need to be 
limited to just dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco cta", etc.)
'''

# Brute force would be checking all permutations to see if any are a palindrome. Inefficient
# String that is a palindrome could have the following conditions:
# 1 - each letter in string appears twice ('aabbcc')
# 2 - each letter in string appears an even amount ('aaaabbcc')
# 3 - each letter in string appears an even amount and one letter appears an odd amount ('aabbccd')

from collections import Counter
import string

def pal_perm(s):
	s = string.replace(s," ","")
	s = s.lower()
	s_count = Counter(s)
	oddcount = 0
	evencount = 0
	for count in s_count.itervalues():
		if count == 1 or count % 2 != 0:
			oddcount += 1
		if count % 2 == 0:
			evencount += 1
	# print evencount, oddcount # for testing
	while evencount >= 2:
		if oddcount == 0 or oddcount == 1:
			return True
		else:
			return False
	return False

		

print pal_perm('aabbcc') # True
print pal_perm('aabbbcc') # True
print pal_perm('aaaabbcc') # True
print pal_perm('taco cat') # True
print pal_perm('taco cats') # False
print pal_perm('kkaya') # True
print pal_perm('amanaplanacanalpanama') # True
print pal_perm('aaabbbccc') # False
print pal_perm('Tact Coa') # True
print pal_perm('jhsabckuj ahjsbckj') # True
print pal_perm('Able was I ere I saw Elba') # True
print pal_perm('So patient a nurse to nurse a patient so') # False
print pal_perm('Random Words') # False
print pal_perm('Not a Palindrome') # False
print pal_perm('no x in nixon') # True
print pal_perm('azAZ') # True
