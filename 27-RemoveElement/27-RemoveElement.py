# Last updated: 11/1/2025, 9:35:14 PM
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Counter for elements not equal to val
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Place the non-val element at index k
                k += 1
        return k
