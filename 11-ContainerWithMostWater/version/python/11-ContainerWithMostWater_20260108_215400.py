# Last updated: 1/8/2026, 9:54:00 PM
1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        left = 0
4        right = len(height) - 1
5        max_area = 0
6
7        while left < right:
8            max_area = max(max_area, (right - left) * min(height[left], height[right]))
9
10            if height[left] < height[right]:
11                left += 1
12            else:
13                right -= 1
14
15        return max_area
16
17
18
19            
20
21        