'''
1.6 String Compression: 
Implement a method to perform basic string compression using the counts of repeated characters.
For example, the string 'aabcccccaaa' would become 'a2b1c5a3'. If the "compressed" string would
not become smaller than the original string, your method should return the original string.
You can assume the string has only uppercase and lowercase letters (a-z).
'''

def string_compression(s):
	letter_counts = []
	count = 0
	for letter in range(len(s)):
		if letter != 0 and s[letter] != s[letter - 1]:
			letter_counts.append(s[letter - 1] + str(count))
			count = 0
		count += 1
	letter_counts.append(s[-1] + str(count))
	final = ''.join(letter_counts)
	if len(final) >= len(s):
		return s
	else:
		return final


print string_compression('aabcccccaaa')
print string_compression('abcdef')
print string_compression('sssssssstttttttuuuuttteerrrrrrrrrr')



