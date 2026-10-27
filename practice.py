def bracket_validator(s: str) -> bool:
	pairs = {")": "(", "]": "[", "}": "{"}
	stack = []

	for char in s:
		if char in pairs.values():
			stack.append(char)
		elif char in pairs.keys():
			if not stack or stack[-1] != pairs[char]:
				return False
			stack.pop()
	return len(stack) == 0

# print(bracket_validator("()"))
# print(bracket_validator("()[]{}"))
# print(bracket_validator("(]"))
# print(bracket_validator("((())"))
# print(bracket_validator(""))

def cryptic_sorter(strings: list[str]) -> list[str]:
	def vowels_counter(s: str) -> int:
		count = 0
		vowels = "aeiou"
		for c in s:
			if c in vowels:
				count += 1
		return count

	result = list(strings)

	for i in range(len(result)):		
		for j in range(len(result) - 1 - i):
			swap = False
			w1 = result[j]
			w2 = result[j + 1]

			if len(w1) > len(w2):
				swap = True
			elif len(w1) == len(w2):
				if w1.lower() > w2.lower():
					swap = True
				elif w1.lower() == w2.lower():
					if vowels_counter(w1) > vowels_counter(w2):
						swap = True							
			if swap:
				result[j], result[j + 1] = w2, w1
	return result

# print(cryptic_sorter(["apple","cat","banana","dog","elephant"]))	

def echo_validator(text: str) -> bool:
	return text.replace(" ", "").lower() == text.replace(" ", "").lower()[::-1]

# print(echo_validator("A man a plan a canal Panama"))

def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
	new_list = []

	for l in matrix:
		new_list.append(l[::-1])
	return new_list

# print(mirror_matrix([[1,2,3],[4,5,6]]))

def hidenp(small: str, big: str) -> bool:
	i = 0
	j = 0

	while i < len(small) and j < len(big):
		if small[i] == big[j]:
			i += 1
		j += 1

	return len(small) == i

# print(hidenp("abc", "a1b2c3"))
# print(hidenp("aec", "abcde"))
# print(hidenp("", "abc"))

def inter(s1: str, s2: str) -> str:
	new_str = ""

	for char in s1:
		if char in s2 and char not in new_str:
			new_str += char

	return new_str

# print(inter("hello", "world"))
# print(inter("banana", "band"))	
# print(inter("", "abc"))

def number_base_converter(number: str, from_base: int, to_base: int) -> str:
	digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	if not 2 <= from_base <= 36 or not 2 <= to_base <= 36:
		return "ERROR"

	try:
		decimal = int(number, from_base)

		if decimal == 0:
			return "0"

		result = ""
		while decimal > 0:
			result = digits[decimal % to_base] + result
			decimal //= to_base

		return result	
	except ValueError:
		return "ERROR"				

# print(number_base_converter("1010", 2, 10))
# print(number_base_converter("FF", 16, 10))
# print(number_base_converter("255", 10, 16))

def pattern_tracker(text: str) -> int:
	count = 0

	for i in range(len(text) - 1):
		if text[i].isdigit() and text[i + 1].isdigit():
			if int(text[i]) + 1 == int(text[i + 1]):
				count += 1
	return count

# print(pattern_tracker("123"))
# print(pattern_tracker("12a34"))
# print(pattern_tracker("987654321"))	
# print(pattern_tracker("01234567"))

def anagram(s1: str, s2: str) -> bool:
	return sorted(s1.replace(" ", "").lower()) == sorted(s2.replace(" ", "").lower())

# print(anagram("listen", "silent"))	
# print(anagram("hello", "world"))

def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
	merged = list1 + list2
	return sorted(merged)

# print(shadow_merge([1,3,5], [2,4,6]))	
# print(shadow_merge([1,2,3], [4,5,6]))
# print(shadow_merge([1,1,2], [1,3,3]))

def string_permutation_checker(s1: str, s2: str) -> bool:
	return sorted(s1) == sorted(s2)

# print(string_permutation_checker("abc", "bca"))
# print(string_permutation_checker("abc", "def"))	
# print(string_permutation_checker("a gentleman","elegant man"))

def string_sculptor(text: str) -> str:
	result = ""
	to_lower = True

	for char in text:
		if char.isalpha():
			if to_lower:
				result += char.lower()
			else:
				result += char.upper()
			to_lower = not to_lower
		else:
			result += char

	return result	

# print(string_sculptor("hello"))	
# print(string_sculptor("Hello World"))		

def twist_sequence(arr: list[int], k: int) -> list[int]:
	if not arr:
		return arr

	k = k % len(arr)

	if k == 0:
		return arr	

	return arr[-k:] + arr[:-k]

# print(twist_sequence([1,2,3,4,5], 2))	
# print(twist_sequence([1,2,3], 1))	
# print(twist_sequence([1,2,3,4], 0))

def whisper_cipher(text: str, shift: int) -> str:
	base_lower = "abcdefghijklmnopqrstuvwxyz"
	base_upper = base_lower.upper()
	result = ""

	for char in text:
		if char.isalpha():
			if char.islower():
				new_index = (base_lower.index(char) + shift) % 26
				new_char = base_lower[new_index]
			if char.isupper():
				new_index = (base_upper.index(char) + shift) % 26
				new_char = base_upper[new_index]
			result += new_char	
		else:
			result += char	
	return result		

# print(whisper_cipher("hello", 3))	
# print(whisper_cipher("Hello World!", 1))
# print(whisper_cipher("abc", -3))			
