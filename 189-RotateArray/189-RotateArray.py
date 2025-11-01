# Last updated: 11/1/2025, 9:34:17 PM
from collections import deque
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        for _ in range(k):
            nums.insert(0, nums.pop())

        
