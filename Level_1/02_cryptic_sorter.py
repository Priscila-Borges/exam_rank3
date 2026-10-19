"""
Write a function that sorts a list of strings according to multiple criteria:
1. Primary sort: By string length (shortest first)
2. Secondary sort: ASCII order, except letters are compared case-insensitively
   (for strings of same length)
3. Tertiary sort: By number of vowels (ascending, for same length and lexically equal)
4. Equal strings will appear in the same order as in the input list.

Forbidden functions: sorted(), list.sort()
"""

def cryptic_sorter(strings: list[str]) -> list[str]:
	sorted_list = list(strings)
	length = len(sorted_list)

	def count_vowels(s: str) -> int:
		vowels = "aeiou"
		count = 0

		for char in s:
			if char.lower() in vowels:
				count += 1

		return count

	for i in range(length):
		for j in range(length - 1 - i):
			word1 = sorted_list[j]
			word2 = sorted_list[j+1]

			swap = False

			if len(word1) > len(word2):
				swap = True

			elif len(word1) == len(word2):
				if word1.lower() > word2.lower():
					swap = True

				elif word1.lower() == word2.lower():	
					if count_vowels(word1) > count_vowels(word2):
						swap = True
			if swap:
				sorted_list[j], sorted_list[j+1] = word2, word1

	return sorted_list


print(cryptic_sorter(["apple","cat","banana","dog","elephant"]))
print(cryptic_sorter(["aaa","bbb","AAA","BBB"]))
print(cryptic_sorter(["hello","world","hi","test"]))
print(cryptic_sorter([]))
		