# Last updated: 11/1/2025, 9:33:58 PM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp = [1] * len(nums)
        
        left = 1
        for i in range(len(nums)):
            temp[i] *= left
            left *= nums[i]
        
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            temp[i] *= right
            right *= nums[i]
    
        return temp        