# Problem 2: Echo Validate (Palindrome)
# Write a function that checks if a string is a palindrome.
# Ignore spaces and case

# Return True if palindrome, False otherwise
# Examples:
# "racecar" → True
# "A man a plan a canal Panama" → True (ignoring spaces and case)
# "hello" → False

def is_palindrome(string: str) -> bool:
	cleaned = ""
	for char in string:
		if not char.isspace():
			cleaned += char.lower()

	return cleaned == cleaned[::-1]

print(is_palindrome("racecar"))
print(is_palindrome("A man a plan a canal Panama" ))
print(is_palindrome("hello"))