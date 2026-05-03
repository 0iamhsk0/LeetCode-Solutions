# Last updated: 5/3/2026, 7:57:27 PM
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        len_s, len_p = len(s), len(p)

        if len_p > len_s:
            return res

        p_count = Counter(p)
        window_count = Counter(s[:len_p])

        if window_count == p_count:
            res.append(0)

        for i in range(len_s - len_p):
            left = s[i]
            right = s[i + len_p]

            window_count[left] -= 1
            if window_count[left] == 0:
                del window_count[left]

            window_count[right] += 1

            if window_count == p_count:
                res.append(i + 1)

        return res
