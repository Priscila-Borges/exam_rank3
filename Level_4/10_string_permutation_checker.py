
"""
Write a function that checks if two strings are permutations of each other.

A permutation means same characters, possibly rearranged
Examples:
"abc", "bca" → True
"abc", "def" → False
"aab", "aba" → True
"""

def is_permutation(s1: str, s2: str) -> bool:
	if len(s1) != len(s2):
		return False
	char_count = {}

	for char in s1:
		char_count[char] = char_count.get(char, 0) + 1

	for char in s2:
		if char not in char_count or char_count[char] == 0:
			return False
		char_count[char] -= 1
	
	return True	

# def is_permutation(s1: str, s2: str) -> bool:
# 	return sorted(s1) == sorted(s2)

print(is_permutation("abc", "bca"))  # Output: True
print(is_permutation("abc", "def"))  # Output: False
print(is_permutation("aab", "aba"))  # Output: True