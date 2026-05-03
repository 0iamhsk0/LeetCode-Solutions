# Last updated: 5/3/2026, 7:57:19 PM
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum
        n = len(nums)

        for i in range(n - k):
            window_sum = window_sum - nums[i] + nums[i + k]
            max_sum = max(max_sum, window_sum)

        return max_sum / k
