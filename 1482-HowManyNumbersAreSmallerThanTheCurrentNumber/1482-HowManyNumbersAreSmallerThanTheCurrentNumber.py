# Last updated: 11/1/2025, 9:32:58 PM
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # brute
        # ans = []
        # for i in range(len(nums)):
        #     cnt = 0 #for every new number the count resets
        #     for j in range(len(nums)):
        #         if nums[i] > nums[j]:
        #             cnt += 1
        #     #at the end of the inner loop, just append the resultant cnt to ans
        #     ans.append(cnt)
        # return ans
        #or:
        # return [sorted(nums).index(i) for i in nums]

        #better approach: O(n log n) : hashing + sorting
        sorted_nums = sorted(nums)
        hashmap = {}
        for index, val in enumerate(sorted_nums):
            if val not in hashmap:
                hashmap[val] = index
                #stores the first occurances and removes the dupes
        return [hashmap[num] for num in nums]
            
        

        
                
        