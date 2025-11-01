# Last updated: 11/1/2025, 9:34:06 PM
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # seen = set()
        
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)
        
        # return False
        temp = set(nums)
        if len(temp) == len(nums):
            return False
        else:
            return True
