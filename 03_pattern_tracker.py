"""
Problem 3: Pattern Tracker
Write a function that counts the number of valid consecutive digit pairs
in a string. A valid pair consists of two adjacent digits where the second
digit is exactly one greater than the first.
A 9 followed by a 0 is NOT a valid pair.

Your function must be declared as follows:

    def pattern_tracker(text: str) -> int:

Examples:
    pattern_tracker("123")        -> 2
    pattern_tracker("12a34")      -> 2
    pattern_tracker("987654321")  -> 0
    pattern_tracker("01234567")   -> 7
    pattern_tracker("abc")        -> 0
    pattern_tracker("1a2b3c4")    -> 0
    pattern_tracker("112233")     -> 2
"""

def pattern_tracker(text: str) -> int:
	counter = 0
	for i in range(len(text) - 1):
		if text[i].isdigit() and text[i + 1].isdigit():
			if int(text[i]) + 1 == int(text[i + 1]):
				counter += 1

	return counter

print(pattern_tracker("123"))
print(pattern_tracker("12a34"))
print(pattern_tracker("987654321"))	
print(pattern_tracker("01234567"))
print(pattern_tracker("abc"))
print(pattern_tracker("1a2b3c4"))
print(pattern_tracker("112233"))
