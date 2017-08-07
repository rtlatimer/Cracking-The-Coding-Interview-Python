'''
1.3 URLify:
Write a method to replace all spaces in a string with '%20'.
You may assume that the string has sufficient space at the end to hold
the additional characters, and that you are given the "true" length of
the string.
EXAMPLE:
Input: "Mr John Smith    ", 13
Output: "Mr%20John%20Smith"
'''

import re

def urlify(s):
	s_stripped = s.strip()
	s_cleaned = re.sub(' +','%20',s_stripped)
	return s_cleaned

print urlify('Mr John   Smith    ')
print urlify('  URLify    is    an awesome    program!      ')
