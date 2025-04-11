from typing import List

def triplet_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()  # Sorting helps in avoiding duplicates and using two-pointer technique
    res = []
    n = len(nums)

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates for the first element
            continue

        left, right = i + 1, n - 1  # Two-pointer setup
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == 0:
                res.append([nums[i], nums[left], nums[right]])

                # Skip duplicates for the second and third elements
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif current_sum < 0:
                left += 1  # Increase sum by moving left pointer
            else:
                right -= 1  # Decrease sum by moving right pointer

    return res

# Test Case
print(triplet_sum([0, -1, 2, -3, 1]))  # Output: [[-3, 1, 2], [-1, 0, 1]]
