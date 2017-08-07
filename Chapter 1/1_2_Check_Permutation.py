'''
1.2 Check Permutation:
Given two strings, write a method to decide if one is a permutation of the other.
'''
from collections import Counter

def check_permutation(s,t):
	s_count = Counter(s)
	t_count = Counter(t)
	if s_count == t_count:
		return True
	else:
		return False

print check_permutation('robert', 'trebor')
print check_permutation('banana', 'orange')
print check_permutation('abcd', 'abc')
print check_permutation('abcd', 'dbca')