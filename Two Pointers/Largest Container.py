from typing import List

def largest_container(heights: List[int]) -> int:
    left, right = 0, len(heights) - 1
    max_water = 0

    while left < right:
        # Calculate the area
        height = min(heights[left], heights[right])
        width = right - left
        max_water = max(max_water, height * width)

        # Move the pointer pointing to the smaller height
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_water

# Test case
print(largest_container([2, 7, 8, 3, 7, 6]))  # Output: 24
