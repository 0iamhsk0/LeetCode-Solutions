# Last updated: 1/9/2026, 4:32:30 PM
1class Solution:
2    def findMaxAverage(self, nums: List[int], k: int) -> float:
3        window_sum = sum(nums[:k])
4        max_sum = window_sum
5        n = len(nums)
6
7        for i in range(n - k):
8            window_sum = window_sum - nums[i] + nums[i + k]
9            max_sum = max(max_sum, window_sum)
10
11        return max_sum / k
12