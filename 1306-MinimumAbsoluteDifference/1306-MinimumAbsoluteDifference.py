# Last updated: 11/1/2025, 9:33:06 PM
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        #window size = 2
        arr.sort()
        #finding the min diff:
        min_diff = float('inf')
        for i in range(1, len(arr)):
            min_diff = min(min_diff, arr[i] - arr[i-1])
        
        #moving the window for storing the pairs
        ans = []
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] == min_diff:
                ans.append([arr[i-1], arr[i]])
        return ans

