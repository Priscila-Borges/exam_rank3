"""
Write a function that checks if a string is a palindrome,
ignoring spaces and case, only consider alphabetic characters
for the comparison.
Function signature
def echo_validator(text: str) -> bool:
"""

def echo_validator(text: str) -> bool:
	if not text:
		return False

	cleaned = ""
	for char in text:
		if not char.isspace():
			cleaned += char.lower()

	return cleaned == cleaned[::-1]
		
print(echo_validator("racecar")) # Expected: True
print(echo_validator("A man a plan a canal Panama")) # Expected: True
print(echo_validator("race a car"))	# Expected: False
print(echo_validator("Was it a car or a cat I saw")) # Expected: True
print(echo_validator("hello")) # Expected: False
print(echo_validator("Madam Im Adam")) # Expected: True
print(echo_validator("madam")) # Expected: True
print(echo_validator("Able was I ere I saw Elba")) # Expected: True
print(echo_validator("")) # Expected: False
