# Last updated: 1/9/2026, 4:33:01 PM
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
      curSum = maxSum = sum(nums[:k])

      l = 0

      for r in range(k, len(nums)):
        curSum -= nums[l]
        curSum += nums[r]
        l += 1

        maxSum = max(curSum, maxSum)
      
      return maxSum/k