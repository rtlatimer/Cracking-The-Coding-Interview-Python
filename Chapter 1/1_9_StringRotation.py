'''
1.9 String Rotation:
Assume you have a method isSubstring which checks if one word is a substring
of another. Given two strings, s1 and s2, write code to check if s2 is a rotation
of s1 using only one call to isSubstring (e.g., "waterbottle" is a rotation
of "erbottlewat").
'''

# input: 2 strings
# output: true or false

from collections import Counter

def isSubstring(s1,s2):
	print "Looking for '{}'' in '{}': ".format(s2, s1)
	if len(s1) != len(s2):
		return False
	s1_dict = Counter(s1)
	s2_dict = Counter(s2)
	if s1_dict != s2_dict:
		return False
	for i in range(len(s1)):
		if s2[i:] + s2[:i] == s1:
			return True
	return False

print isSubstring('waterbottle', 'erbottlewat')
print isSubstring('waterbottle', 'bottlewater')
print isSubstring('waterbottle', 'botwatertle')
