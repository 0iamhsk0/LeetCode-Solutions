# Last updated: 11/1/2025, 9:33:39 PM
from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Sort the greed factors and cookie sizes
        g.sort()
        s.sort()
        
        i = 0  # Pointer for children
        j = 0  # Pointer for cookies
        
        # Try to satisfy as many children as possible
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:  # If the cookie satisfies the child
                i += 1       # Move to the next child
            j += 1           # Always move to the next cookie
        
        return i  # Number of satisfied children
