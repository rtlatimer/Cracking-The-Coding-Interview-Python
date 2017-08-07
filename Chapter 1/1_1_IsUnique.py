'''
1.1 Is Unique:
Implement an algorithm to determine if a string has all unique characters. 
What if you cannot use additional data structures?
'''

from collections import Counter

def is_unique(s):
	s_count = Counter(s)
	if any(count >= 2 for count in s_count.itervalues()):
		return False
	else:
		return True

print is_unique('banana')
print is_unique('orange')
print is_unique('robert')
print is_unique('jane')
