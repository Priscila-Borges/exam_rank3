"""
A sequence of numbers is called an arithmetic progression if the difference 
between any two consecutive elements is the same. Given an array of numbers arr, 
return true if the array can be rearranged to form an arithmetic progression. 
Otherwise, return false.

Examples:
[3, 5, 1] → True (can be rearranged to [1, 3, 5] with difference 2)
[1, 2, 4] → False
[1, 3, 5, 7] → True (difference is 2)
"""

def can_make_arithmetic_progression(arr: list[int]) -> bool:
    # 1. Sort the array in place
    arr.sort()
    
    # 2. Calculate the difference between the first two elements
    diff = arr[1] - arr[0]
    
    # 3. Check every subsequent pair
    for i in range(2, len(arr)):
        if arr[i] - arr[i - 1] != diff:
            return False
            
    return True

# Test cases
print(can_make_arithmetic_progression([3, 5, 1]))     # Output: True ([1, 3, 5], diff = 2)
print(can_make_arithmetic_progression([1, 2, 4]))     # Output: False (diffs are 1 and 2)
print(can_make_arithmetic_progression([1, 3, 5, 7]))  # Output: True (diff = 2)