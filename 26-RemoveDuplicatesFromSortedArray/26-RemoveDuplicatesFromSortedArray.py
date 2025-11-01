# Last updated: 11/1/2025, 9:35:15 PM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # edge cases:
        if not nums:
            return 0
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k += 1
        return k
            
