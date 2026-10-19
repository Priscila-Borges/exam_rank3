"""
Write a function that shifts alphabetical characters by a given amount.

Only shift letters (a-z, A-Z)
Preserve case
Other characters remain unchanged
Wraparound: 'z' + 1 = 'a'
Examples:
"hello", shift=3 → "khoor"
"hello world!", shift=3 → "khoor zruog!"
"xyz", shift=3 → "abc"
"ABC", shift=1 → "BCD"
"""

def shift_char(text: str, number: int) -> str:
	result = ""

	for char in text:
		if char.isalpha():
			base = ord('a') if char.islower() else ord('A')

			shifted_code = (ord(char) - base + number) % 26 + base
			result += chr(shifted_code)
		else:
			result += char	

	return result

print(shift_char("hello", 3))        # Output: khoor
print(shift_char("hello world!", 3)) # Output: khoor zruog!
print(shift_char("xyz", 3))          # Output: abc
print(shift_char("ABC", 1))          # Output: BCD
