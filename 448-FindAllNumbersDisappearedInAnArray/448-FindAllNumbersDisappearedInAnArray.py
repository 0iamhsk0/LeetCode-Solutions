# Last updated: 11/1/2025, 9:33:43 PM
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        new_nums = set(nums)
        temp = []
        for i in range(1, len(nums) + 1):
            if not i in new_nums:
                temp.append(i)
        return temp

        