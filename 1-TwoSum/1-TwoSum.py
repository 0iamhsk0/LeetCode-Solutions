# Last updated: 11/1/2025, 9:35:34 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i, num1 in enumerate(nums):
            val = target - num1
            if val in store:
                return [i, store[val]]
            store[num1] = i
        return []
        # use the two pointer approach(only for sorted array)
# from typing import List

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         nums_sorted = sorted((num, i) for i, num in enumerate(nums))  # Sort with original indices
#         left, right = 0, len(nums) - 1
        
#         while left < right:
#             curr_sum = nums_sorted[left][0] + nums_sorted[right][0]
            
#             if curr_sum == target:
#                 return [nums_sorted[left][1], nums_sorted[right][1]]  # Return original indices
#             elif curr_sum < target:
#                 left += 1
#             else:
#                 right -= 1
        
#         return []  # No solution found




