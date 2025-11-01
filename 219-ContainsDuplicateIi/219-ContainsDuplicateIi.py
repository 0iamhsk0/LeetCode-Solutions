# Last updated: 11/1/2025, 9:34:05 PM
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #brute:
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i] == nums[j] or abs(i-j) <= k:
        #             return True
        #         else:
        #             return False

        #using sets or dict:
        # seen = set()
        # for i, num in enumerate(nums):
        #     if num in seen:
        #         return True
        #     else:
        #         seen.add(num)
        #     if len(seen) > k:
        #         seen.remove(nums[i-k]) #which will be the first index
        # return False

        num_index={}
        for index,num in enumerate(nums):
            if num in num_index and abs(index-num_index[num])<=k:
                return True
            else:
                num_index[num]=index        
        return False
    

        