# Last updated: 11/1/2025, 9:34:21 PM
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Using two-pointer approach
        left, right = 0, len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                return [left + 1, right + 1]  # 1-based index
            elif current_sum < target:
                left += 1
            else:
                right -= 1
