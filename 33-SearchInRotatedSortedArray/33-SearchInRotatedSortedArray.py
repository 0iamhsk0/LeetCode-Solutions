# Last updated: 11/1/2025, 9:35:11 PM
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left: int, right: int) -> int:
            if left > right:
                return -1
            
            mid = (left + right) // 2
            
            # Case 1: Target found
            if nums[mid] == target:
                return mid
            
            # Case 2: Left part is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    return binary_search(left, mid - 1)  # Target is in the left sorted half
                else:
                    return binary_search(mid + 1, right)  # Target is in the right unsorted half
            
            # Case 3: Right part is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    return binary_search(mid + 1, right)  # Target is in the right sorted half
                else:
                    return binary_search(left, mid - 1)  # Target is in the left unsorted half
        
        # Initial call to the helper function with full array range
        return binary_search(0, len(nums) - 1)
