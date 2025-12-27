# Last updated: 12/27/2025, 3:46:28 PM
# Method - 1: Sorting, popping and storing

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:    
        ans = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            ans[key].append(s)
        
        return list(ans.values())