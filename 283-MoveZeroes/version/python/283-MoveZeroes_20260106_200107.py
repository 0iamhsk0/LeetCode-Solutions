# Last updated: 1/6/2026, 8:01:07 PM
1#
2class Solution:
3    def moveZeroes(self, nums: List[int]) -> None:
4        """
5        Do not return anything, modify nums in-place instead.
6        """
7        # latest sol
8        left = 0
9        for right in range(0, len(nums)):
10            # swapping 
11            if nums[right] != 0:
12                nums[left], nums[right] = nums[right], nums[left]
13                left += 1
14                        
15        return nums
16
17
18
19        