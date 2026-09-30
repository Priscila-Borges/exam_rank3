# Problem 1: Bracket Validator
# Write a function that validates if brackets are properly matched.
# Valid brackets: (), [], {}
# Other characters are ignored

# Return True if valid, False otherwise
# Examples:
# "()" → True
# "()[]{}" → True
# "{[]}" → True
# "([)]" → False
# "(((" → False
# "abc(def)ghi" → True (non-brackets ignored)

def is_valid_brackets(string: str) -> bool:
	stack = []
	pairs = {")": "(", "]": "[", "}": "{"}

	for char in string:
		if char in pairs.values():
			stack.append(char)
		elif char in pairs.keys():
			if not stack or stack[-1] != pairs[char]:
				return False
			stack.pop()
	return len(stack) == 0	

print(is_valid_brackets("()[]{}"))
print(is_valid_brackets("([)]"))
