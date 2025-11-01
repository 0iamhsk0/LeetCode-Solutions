# Last updated: 11/1/2025, 9:32:37 PM
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        zero_count = 0
        zero_seq_count = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zero_seq_count += 1
            else:
                zero_seq_count = 0
            zero_count += zero_seq_count
        
        return zero_count