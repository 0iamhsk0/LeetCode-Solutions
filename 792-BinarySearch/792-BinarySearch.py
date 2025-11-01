# Last updated: 11/1/2025, 9:33:27 PM

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid 
            elif nums[mid] < target:
                left = mid + 1  
            else:
                right = mid - 1 
        
        return -1 
