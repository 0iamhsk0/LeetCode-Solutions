# Last updated: 11/1/2025, 9:35:09 PM
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            center = (left + right) // 2
            if nums[center] == target:
                return center
            elif nums[center] < target:
                left = center + 1
            else:
                right = center - 1
        return left      