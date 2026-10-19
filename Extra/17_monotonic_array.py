"""
An array is monotonic if it is either monotone increasing or monotone decreasing.
An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]

An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j]
Given an integer array nums, return true if the array is monotonic, or false otherwise.

Examples:
[1, 2, 2, 3] → True (increasing)
[6, 5, 4, 4] → True (decreasing)
[1, 3, 2] → False (neither)
[3, 3, 3, 3] → True (both increasing and decreasing)
"""

def is_monotonic(nums: list[int]) -> bool:
    increasing = True
    decreasing = True
    
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            increasing = False
        if nums[i] < nums[i + 1]:
            decreasing = False
            
    # If it survived either test, it is monotonic
    return increasing or decreasing

# Test cases
print(is_monotonic([1, 2, 2, 3]))    # Output: True (increasing)
print(is_monotonic([6, 5, 4, 4]))    # Output: True (decreasing)
print(is_monotonic([1, 3, 2]))       # Output: False (went up then down)
print(is_monotonic([3, 3, 3, 3]))    # Output: True (both)
