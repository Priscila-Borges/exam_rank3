"""
Given an integer array nums, move all 0's to the end while maintaining the 
relative order of the non-zero elements. Note: You must do this in-place without 
making a copy of the array.

Examples:
[0, 1, 0, 3, 12] → [1, 3, 12, 0, 0]
[0] → [0]
[1, 2, 3] → [1, 2, 3]
"""

def move_zeroes(nums: list[int]) -> None:
    insert_pos = 0
    
    for i in range(len(nums)):
        if nums[i] != 0:
            # Swap the non-zero element to the front insert position
            nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
            insert_pos += 1

# Test cases (modifies the list in-place)
arr1 = [0, 1, 0, 3, 12]
move_zeroes(arr1)
print(arr1)  # Output: [1, 3, 12, 0, 0]

arr2 = [0]
move_zeroes(arr2)
print(arr2)  # Output: [0]

arr3 = [1, 2, 3]
move_zeroes(arr3)
print(arr3)  # Output: [1, 2, 3]
