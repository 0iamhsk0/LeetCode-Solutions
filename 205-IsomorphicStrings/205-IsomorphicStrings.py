# Last updated: 11/1/2025, 9:34:11 PM
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # Approach - 1: Two hashmaps
        hash_map_s = dict()
        hash_map_t = {}

        for i in range(len(s)):
            if s[i] not in hash_map_s:
                hash_map_s[s[i]] = i

            if t[i] not in hash_map_t:
                hash_map_t[t[i]] = i

            if hash_map_s[s[i]] != hash_map_t[t[i]]:
                return False
        return True

        ## Approach - 2: One hashmap
        # hash_map = {}

        # for i, j in zip(s, t):
        #     if i in hash_map:
        #         if hash_map[i] != j:
        #             return False

        #     elif j in hash_map.values():
        #         return False
            
        #     hash_map[i] = j
        
        # return True
    
        ## Approach 3: Using set
        # return len(set(s)) == len(set(t)) == len(set(zip(s,t)))


