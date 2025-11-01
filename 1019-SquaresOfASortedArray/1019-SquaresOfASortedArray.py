# Last updated: 11/1/2025, 9:33:22 PM
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # #brute force:
        # #traverse the array till len(nums) - 1:
        #     #1st case: if ele = 0 or -ve return 0 (append)
        #     #2nd case: non -ve, return square of that number (append)
        res = [0] * len(nums)
        # for i in range(0, len(nums)):
        #     # if nums[i] == 0 or nums[i] < 0:
        #     #     ans.append(nums[i])
        #     # else:
        #     ans.append(nums[i] ** 2)
        #     ans.sort()
        # return ans
        left = 0
        right = len(nums) - 1
        #comparing left and right squares as we move on
        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                res[i] = nums[left] ** 2
                left += 1
            else:
                res[i] = nums[right] ** 2
                right -= 1
        
        return res

                
        