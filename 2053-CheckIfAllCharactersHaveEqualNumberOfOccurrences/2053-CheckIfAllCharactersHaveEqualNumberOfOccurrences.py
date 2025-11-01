# Last updated: 11/1/2025, 9:32:44 PM
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = {}
        for i in s: 
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        all_vals = d.values()
        return len(set(all_vals)) == 1
