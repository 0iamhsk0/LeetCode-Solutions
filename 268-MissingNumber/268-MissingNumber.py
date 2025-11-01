# Last updated: 11/1/2025, 9:33:55 PM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # # Calculate the expected sum of numbers from 0 to n
        # n = len(nums)
        # sum_n = n * (n + 1) // 2
        # sum_nums = sum(nums)
        # return sum_n - sum_nums
        
        #approach 2: O(nlogn)
        nums.sort()
        for k, v in enumerate(nums):
            if k != v:
                return v-1
            #if reaches to the end:
            if v == len(nums)-1:
                return v+1
        