# Write a function that checks if the brackets in a string are valid.

# A string is valid if every opening bracket has a matching closing bracket
# in the correct order.

# Allowed brackets: (), [], {}
# Other characters are ignored

# Return True if valid, False otherwise

def bracket_validator(s: str) -> bool:
	stack = []
	pairs = {")": "(", "]": "[", "}": "{"}

	for char in s:
		if char in pairs.values():
			stack.append(char)
		elif char in pairs.keys():
			if not stack or stack[-1] != pairs[char]:
				return False
			stack.pop()		
	return len(stack) == 0

print(bracket_validator("()"))
print(bracket_validator("()[]{}"))
print(bracket_validator("(]"))
print(bracket_validator("([)]"))
print(bracket_validator("{[]}"))
print(bracket_validator("hello(world)"))
print(bracket_validator("((())"))
print(bracket_validator(""))
