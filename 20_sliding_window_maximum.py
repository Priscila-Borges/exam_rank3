# Problem 20: Sliding Window Maximum

# Write a function that finds the maximum value in every sliding window of
# size k in an array.

# Function signature:

# def sliding_window_maximum(nums: list[int], k: int) -> list[int]:

# Requirements:

# Slide a window of size k across the array from left to right
# For each window, find the maximum element
# Return a list containing the maximum value from each window
# Handle edge cases:
# empty array
# invalid k
# k > len(nums)

# If input is invalid, return:

# []

# Examples:

# Example 1:

# nums = [1, 3, -1, -3, 5, 3, 6, 7]
# k = 3

# Windows:

# [1, 3, -1] -> 3
# [3, -1, -3] -> 3
# [-1, -3, 5] -> 5
# [-3, 5, 3] -> 5
# [5, 3, 6] -> 6
# [3, 6, 7] -> 7

# Result:

# [3, 3, 5, 5, 6, 7]

# Example 2:

# nums = [4, 2, 1]
# k = 1

# Result:

# [4, 2, 1]

# Example 3:

# nums = [9, 5, 2]
# k = 5

# Result:

# []

# Invalid window size.

# Example 4:

# nums = []
# k = 3

# Result:

# []

# This problem tests:

# sliding window technique
# queue/deque reasoning
# window boundary management
# efficient maximum tracking.