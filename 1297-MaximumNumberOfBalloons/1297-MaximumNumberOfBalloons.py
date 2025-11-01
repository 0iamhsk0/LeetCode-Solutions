# Last updated: 11/1/2025, 9:33:07 PM
from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        return min(count['b'], count['a'], count['l'] // 2, count['o'] // 2, count['n'])