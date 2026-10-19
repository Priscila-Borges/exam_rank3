"""
Write a function that rotates an array to the right by k positions.

Last k elements move to the front
Examples:
[1, 2, 3, 4, 5], k=2 → [4, 5, 1, 2, 3]
[1, 2, 3, 4, 5], k=3 → [3, 4, 5, 1, 2]
[1, 2], k=1 → [2, 1]
"""

def twist_sequence(arr: list[int], k: int) -> list[int]:
	if not arr:
		return arr

	k = k % len(arr)
	if k == 0:
		return list(arr)

	return arr[-k:] + arr[:-k]

print(twist_sequence([1, 2, 3, 4, 5], 2))
