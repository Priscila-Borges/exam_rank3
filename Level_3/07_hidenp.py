"""
Write a function that checks if the string 'small' is a subsequence
of 'big'. A subsequence means all characters of 'small' appear in 'big'
in the same order, but not necessarily consecutively.
Function is case-sensitive.

Function signature
def hidenp(small: str, big: str) -> bool:
"""

def hidenp(small: str, big: str) -> bool:
	i = 0
	j = 0
	while i < len(big) and j < len(small):
		if big[i] == small[j]:
			j += 1
		i += 1

	return j == len(small)

print(hidenp("abc", "a1b2c3"))
print(hidenp("ace", "abcde"))
print(hidenp("aec", "abcde"))
print(hidenp("", "abc"))
print(hidenp("abc", "ab"))
print(hidenp("aaaa", "aaa"))
