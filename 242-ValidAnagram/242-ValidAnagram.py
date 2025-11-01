# Last updated: 11/1/2025, 9:33:57 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)   