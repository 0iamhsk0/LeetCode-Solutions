# Last updated: 11/1/2025, 9:32:35 PM
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        seen = set()
        window_sum = 0
        max_sum = 0
        left = 0

        for right in range(len(nums)):
            # If duplicate found, shrink window from left
            while nums[right] in seen:
                seen.remove(nums[left])
                window_sum -= nums[left]
                left += 1

            # Add current element to window
            seen.add(nums[right])
            window_sum += nums[right]

            # If window size exceeds k, shrink from left
            if right - left + 1 > k:
                seen.remove(nums[left])
                window_sum -= nums[left]
                left += 1

            # If valid window of size k, check for max
            if right - left + 1 == k:
                max_sum = max(max_sum, window_sum)

        return max_sum
