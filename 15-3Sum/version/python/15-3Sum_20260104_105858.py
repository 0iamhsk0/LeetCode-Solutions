# Last updated: 1/4/2026, 10:58:58 AM
1# Approach - 1:
2class Solution:
3    def threeSum(self, nums: List[int]) -> List[List[int]]:
4        # latest sol
5        ans = []
6        nums.sort()
7
8        for i, a in enumerate(nums):
9            if i > 0 and a == nums[i - 1]:
10                continue
11
12            left, right = i + 1, len(nums) - 1
13            while left < right:
14                three_sum = a + nums[left] + nums[right]
15
16                if three_sum > 0:
17                    right -= 1
18                elif three_sum < 0:
19                    left += 1
20                else:
21                    ans.append([a, nums[left], nums[right]])
22                    left += 1
23                    while nums[left] == nums[left - 1] and left < right:
24                        left += 1
25        
26        return ans
27
28
29# # Approach - 2
30# class Solution:
31#     def threeSum(self, nums: List[int]) -> List[List[int]]:
32#         nums.sort()
33#         ans = []
34#         n = len(nums)
35
36#         for i in range(n):
37#             if i > 0 and nums[i] == nums[i - 1]:
38#                 continue     
39
40#             left, right = i + 1, n - 1
41
42#             while left < right:
43#                 current_sum = nums[i] + nums[left] + nums[right]
44                
45#                 if current_sum == 0:
46#                     ans.append([nums[i], nums[left], nums[right]])
47#                     left += 1
48#                     right -= 1
49#                     # Skip duplicates for the second and third elements
50#                     while left < right and nums[left] == nums[left - 1]:
51#                         left += 1
52#                     while left < right and nums[right] == nums[right + 1]:
53#                         right -= 1
54#                 elif current_sum < 0:
55#                     left += 1
56#                 else:
57#                     right -= 1
58        
59#         return ans
60