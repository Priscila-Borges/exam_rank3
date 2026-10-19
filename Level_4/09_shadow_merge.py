"""
Write a function that merges two sorted lists into one sorted list.
Examples:
[1, 3, 5], [2, 4, 6] → [1, 2, 3, 4, 5, 6]
[1, 2, 3], [4, 5, 6] → [1, 2, 3, 4, 5, 6]
[], [1, 2] → [1, 2]

def merge_list(list1: list[int], list2: list[int]) -> list[int]:
	merged = []	

	for i in range(len(list1)):
		merged.append(list1[i])
	for i in range(len(list2)):
		merged.append(list2[i])
	
	for i in range(len(merged)):		
		for j in range(len(merged) -1 - i):		
			n1 = merged[j]
			n2 = merged[j + 1]
			if n1 > n2:
				merged[1 + j], merged[j] = n1, n2					

	return merged

print(merge_list([1, 3, 5], [6, 4, 2]))
"""


def merge_list(list1: list[int], list2: list[int]) -> list[int]:
	merged = list1 + list2
	
	for i in range(len(merged)):		
		for j in range(len(merged) -1 - i):		
			n1 = merged[j]
			n2 = merged[j + 1]
			if n1 > n2:
				merged[1 + j], merged[j] = n1, n2					

	return merged

print(merge_list([1, 3, 5], [6, 4, 2]))
