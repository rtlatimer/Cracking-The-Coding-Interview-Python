'''
1.5 One Away:
There are three types of edits that can be performed on strings:
insert a character, remove a character, or replace a character.
Given two strings, write a function to check if they are one edit
(or zero edits) away:
EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false
'''
# Insert a character: all characters from string 1 will be in string 2. String 2 length will be 1 longer.
# Remove a character: all characters from string 2 will be in string 1. String 1 length will be 1 longer.
# Replace a character: lengths will be the same. All but one character will be identical.

from collections import Counter

def one_away(s,t):
	if s == t:
		return True
	s_count = Counter(s)
	t_count = Counter(t)
	if t_count.viewitems() <= s_count.viewitems() or t_count.keys() == s_count.keys():
		if len(t) == (len(s) - 1):
			return True
	if s_count.viewitems() <= t_count.viewitems() or t_count.keys() == s_count.keys():
		if len(s) == (len(t) - 1):
			return True
	elif len(s) == len(t):
		diff_count = 0
		for char in s:
			if char not in t:
				diff_count +=1
		if diff_count == 1 or diff_count == 0:
			return True
		else:
			return False
	return False

print one_away('pale', 'ple') # True
print one_away('pales', 'pale') # True
print one_away('pale', 'bale') # True
print one_away('pale', 'bake') # False
print one_away('pale', 'pale') # True
print one_away('paleabc', 'pleabc') # True
print one_away('pale', 'ble') # False
print one_away('a', 'b') # True
print one_away('', 'd') # True
print one_away('d', 'de') # True
print one_away('pale', 'pale') # True
print one_away('pale', 'ple') # True
print one_away('ple', 'pale') # True
print one_away('pale', 'bale') # True
print one_away('pale', 'bake') # False
print one_away('pale', 'pse') # False
print one_away('ples', 'pales') # True
print one_away('pale', 'pas') # False
print one_away('pas', 'pale') # False
print one_away('pale', 'pkle') #True
print one_away('pkle', 'pable')# False
print one_away('pal', 'palks') #False
print one_away('palks', 'pal') # False


