# Last updated: 11/1/2025, 9:33:54 PM
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        paper_counts = [0] * (n + 1)
        h = n

        for i in citations[:]:
            paper_counts[min(n, i)] += 1
        
        papers = paper_counts[n]
        while papers < h:
            h -= 1
            papers += paper_counts[h]

        return h
        