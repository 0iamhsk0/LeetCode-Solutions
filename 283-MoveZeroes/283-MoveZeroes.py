# Last updated: 11/1/2025, 9:33:52 PM
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        #moving all non zero elements to the left
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
        return nums




        