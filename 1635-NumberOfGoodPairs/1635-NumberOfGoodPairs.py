# Last updated: 11/1/2025, 9:32:54 PM
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hash_map = {}
        cnt = 0
        for i in nums:
            if i in hash_map:
                cnt += hash_map[i]
                hash_map[i] += 1
            else:
                hash_map[i] = 1

        return cnt
        

        