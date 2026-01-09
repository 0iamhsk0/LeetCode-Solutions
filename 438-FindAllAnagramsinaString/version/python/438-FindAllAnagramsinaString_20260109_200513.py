# Last updated: 1/9/2026, 8:05:13 PM
1from collections import Counter
2
3class Solution:
4    def findAnagrams(self, s: str, p: str) -> List[int]:
5        res = []
6        len_s, len_p = len(s), len(p)
7
8        if len_p > len_s:
9            return res
10
11        p_count = Counter(p)
12        window_count = Counter(s[:len_p])
13
14        if window_count == p_count:
15            res.append(0)
16
17        for i in range(len_s - len_p):
18            left = s[i]
19            right = s[i + len_p]
20
21            window_count[left] -= 1
22            if window_count[left] == 0:
23                del window_count[left]
24
25            window_count[right] += 1
26
27            if window_count == p_count:
28                res.append(i + 1)
29
30        return res
31