from typing import List

def pair_sum_sorted(nums: List[int], target: int) -> List[int]:
    left, right = 0, len(nums) - 1  # Initialize two pointers

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return [left, right]  # Return indices of the pair
        elif current_sum < target:
            left += 1  # Move left pointer forward to increase the sum
        else:
            right -= 1  # Move right pointer backward to decrease the sum

    return []  # Return empty list if no pair is found

# Test Cases
print(pair_sum_sorted([-5, -2, 3, 4, 6], 7))  # Output: [2, 3]
print(pair_sum_sorted([1, 1, 1], 2))         # Output: [0, 1] or other valid pairs
