# Problem 2: Echo Validate (Palindrome)
# Write a function that checks if a string is a palindrome,
# ignoring spaces and case, only consider alphabetic characters
# for the comparison.
# Function signature
# def echo_validator(text: str) -> bool:

def echo_validator(text: str) -> bool:
	cleaned = ""
	for char in text:
		if not char.isspace():
			cleaned += char.lower()

	return cleaned == cleaned[::-1]

print(echo_validator("racecar"))
print(echo_validator("A man a plan a canal Panama"))
print(echo_validator("race a car"))
print(echo_validator("Was it a car or a cat I saw"))
print(echo_validator("hello"))