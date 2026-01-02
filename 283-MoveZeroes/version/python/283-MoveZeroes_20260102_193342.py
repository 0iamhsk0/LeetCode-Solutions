# Last updated: 1/2/2026, 7:33:42 PM
1class Solution:
2    def moveZeroes(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        # latest sol
7        left = 0
8        for right in range(0, len(nums)):
9            # swapping 
10            if nums[right] != 0:
11                nums[left], nums[right] = nums[right], nums[left]
12                left += 1
13                # right += 1
14            else:
15                right += 1
16        
17        return nums
18
19
20
21        