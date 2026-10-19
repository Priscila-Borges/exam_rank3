"""
Write a function that finds the maximum value in every sliding window of
size k in an array.

Function signature:

def sliding_window_maximum(nums: list[int], k: int) -> list[int]:

Requirements:

Slide a window of size k across the array from left to right
For each window, find the maximum element
Return a list containing the maximum value from each window
Handle edge cases:
empty array
invalid k
k > len(nums)

If input is invalid, return:

[]

Examples:

Example 1:

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

Windows:

[1, 3, -1] -> 3
[3, -1, -3] -> 3
[-1, -3, 5] -> 5
[-3, 5, 3] -> 5
[5, 3, 6] -> 6
[3, 6, 7] -> 7

Result:

[3, 3, 5, 5, 6, 7]

Example 2:

nums = [4, 2, 1]
k = 1

Result:

[4, 2, 1]

Example 3:

nums = [9, 5, 2]
k = 5

Result:

[]

Invalid window size.

Example 4:

nums = []
k = 3

Result:

[]

This problem tests:

sliding window technique
queue/deque reasoning
window boundary management
efficient maximum tracking.
"""

from collections import deque

def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
    # Handle edge cases as requested
    if not nums or k <= 0 or k > len(nums):
        return []
        
    result = []
    dq = deque() # Stores indices of elements, not the values themselves
    
    for i in range(len(nums)):
        # 1. Remove indices that have fallen out of the current window's left boundary
        if dq and dq[0] <= i - k:
            dq.popleft()
            
        # 2. Remove smaller elements from the back because they can never be the max 
        # while the current larger element is around
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()
            
        # 3. Add the current element's index to the back
        dq.append(i)
        
        # 4. Once our window has reached size k, record the maximum (which is always at dq[0])
        if i >= k - 1:
            result.append(nums[dq[0]])
            
    return result

# Test cases
print(sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3))  # [3, 3, 5, 5, 6, 7]
print(sliding_window_maximum([4, 2, 1], 1))                   # [4, 2, 1]
print(sliding_window_maximum([9, 5, 2], 5))                   # []
print(sliding_window_maximum([], 3))                          # []
