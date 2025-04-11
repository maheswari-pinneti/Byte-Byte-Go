from typing import List

def shift_zeros_to_the_end(nums: List[int]) -> None:
    non_zero = 0  # Pointer for the position of the next non-zero element
    
    # Move non-zero elements to the front
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero], nums[i] = nums[i], nums[non_zero]
            non_zero += 1

# Test case
nums = [0, 1, 0, 3, 2]
shift_zeros_to_the_end(nums)
print(nums)  # Output: [1, 3, 2, 0, 0]

