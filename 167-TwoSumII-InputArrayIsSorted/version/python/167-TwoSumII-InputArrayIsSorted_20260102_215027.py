# Last updated: 1/2/2026, 9:50:27 PM
1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        # latest sol
4        left = 0
5        right = len(numbers) - 1
6        
7        while left < right:
8            current_sum = numbers[left] + numbers[right]   
9
10            if current_sum == target:
11                return [left + 1, right + 1]
12            if current_sum < target:
13                left += 1
14            else:
15                right -= 1
16        
17        return []