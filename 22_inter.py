# Write a function that returns a string with the characters that appear
# in both strings, without repetitions. Characters are added in the order
# they appear in the first string.

# Function signature
# def inter(s1: str, s2: str) -> str:

def inter(s1: str, s2: str) -> str:
	result = ""
	
	for char in s1:
		if char in s2 and char not in result:
			result += char

	return result

print(inter("hello", "world"))
print(inter("banana", "band"))
print(inter("abcabc", "bc"))
print(inter("abc", "xyz"))
print(inter("", "abc"))
