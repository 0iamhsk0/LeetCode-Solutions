# Last updated: 11/1/2025, 9:35:22 PM
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the array
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n):
            # Skip duplicates for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers to find the remaining two numbers
            target = -nums[i]
            left, right = i + 1, n - 1

            while left < right:
                current_sum = nums[left] + nums[right]
                if current_sum == target:
                    result.append([nums[i], nums[left], nums[right]])
                    # Move the left pointer to the next different number
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Move the right pointer to the next different number
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return result
