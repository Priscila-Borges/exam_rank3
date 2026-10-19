"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Examples:
s = "anagram", t = "nagaram" → True
s = "rat", t = "car" → False
s = "listen", t = "silent" → True
"""

def anagram(s1: str, s2: str) -> bool:
	str1 = s1.replace(" ", "").lower()
	str2 = s2.replace(" ", "").lower()
	return sorted(str1) == sorted(str2)

print(anagram("listen", "silent"))
print(anagram("Triangle", "Integral"))
print(anagram("Dormitory", "Dirty Room"))
print(anagram("hello", "world"))
print(anagram("", ""))
print(anagram("abc", "abcc"))
