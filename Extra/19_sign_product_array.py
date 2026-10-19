"""
Implement a function signFunc(x) that returns:

1 if x is positive
-1 if x is negative
0 if x is equal to 0
You are given an integer array nums. Let product be the product of all values in the array. Return signFunc(product).

Examples:
[-1, -2, -3, -4, 3, 2, 1] → 1
[1, 5, 0, 2, -3] → 0
[-1, 1, -1, 1, -1] → -1
"""

def array_sign(nums: list[int]) -> int:
    negative_count = 0
    
    for num in nums:
        if num == 0:
            return 0  # Any zero makes the whole product zero!
        if num < 0:
            negative_count += 1
            
    # If the count of negatives is odd, return -1. Otherwise, return 1.
    if negative_count % 2 != 0:
        return -1
    else:
        return 1

# Test cases
print(array_sign([-1, -2, -3, -4, 3, 2, 1]))  # Output: 1 (4 negatives, even count)
print(array_sign([1, 5, 0, 2, -3]))           # Output: 0 (contains 0)
print(array_sign([-1, 1, -1, 1, -1]))         # Output: -1 (3 negatives, odd count)
