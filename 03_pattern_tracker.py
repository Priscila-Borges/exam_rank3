# Problem 3: Pattern Tracker
# Write a function that counts consecutive number pairs in a string where the second digit is 1 greater than the first (0-9).
# Examples:
# "abc123def" → 2 (pairs: "12" and "23")
# "456789" → 5 (pairs: "45", "56", "67", "78")
# "abc987def" → 1 (pair: "87")
# "135" → 0 (no consecutive pairs)

def count_consecuive_pairs(string: str) -> int:
	digits = []
	for char in string:
		if char.isdigit():
			digits.append(char)
	
	count = 0
	for i in range(len(digits) - 1):
		if int(digits[i + 1]) == int(digits[i]) + 1:
			count += 1

	return count

print(count_consecuive_pairs("abc123def"))
print(count_consecuive_pairs("456789"))	
print(count_consecuive_pairs("abc987def"))	
print(count_consecuive_pairs("135"))			
