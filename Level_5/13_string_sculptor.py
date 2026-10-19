"""
Write a function that alternates character cases.

1st alphabetical character: lowercase
2nd alphabetical character: uppercase
3rd alphabetical character: lowercase
Continue alternating...
Non-alphabetical characters are unchanged but don't affect the alternation count
Examples:
"hello" → "hElLo"
"abc" → "aBc"
"a1b2c3" → "a1B2c3"
"""

def string_sculptor(text: str) -> str:
	result = ""
	make_lower = True

	for char in text:
		if char.isalpha():
			if make_lower:
				result += char.lower()
			else:
				result += char.upper()
			make_lower = not make_lower	
		else:
			result += char

	return result

print(string_sculptor("hello"))    # Output: hElLo
print(string_sculptor("abc"))      # Output: aBc
print(string_sculptor("a1b2c3"))   # Output: a1B2c3
