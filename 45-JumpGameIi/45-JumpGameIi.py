# Last updated: 11/1/2025, 9:35:07 PM
class Solution:
    def jump(self, nums: List[int]) -> int:
        current_end = jumps = farthest = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            
            if i == current_end:
                jumps += 1
                current_end = farthest
                
        return jumps