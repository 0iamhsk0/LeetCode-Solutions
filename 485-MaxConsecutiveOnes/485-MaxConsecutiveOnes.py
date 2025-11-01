# Last updated: 11/1/2025, 9:33:38 PM
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        cnt_max = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
            else:
                cnt = 0
            cnt_max = max(cnt, cnt_max)
        return cnt_max

            
        