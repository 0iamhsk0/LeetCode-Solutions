# Last updated: 11/1/2025, 9:35:31 PM
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure nums1 is the smaller array to optimize binary search
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        x, y = len(nums1), len(nums2)
        low, high = 0, x
        
        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX
            
            # Edge cases: left and right elements around the partitions
            maxX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minX = float('inf') if partitionX == x else nums1[partitionX]
            
            maxY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minY = float('inf') if partitionY == y else nums2[partitionY]
            
            # Check if we have partitioned correctly
            if maxX <= minY and maxY <= minX:
                # If total length is odd, return the max of left side
                if (x + y) % 2 == 1:
                    return max(maxX, maxY)
                # If total length is even, return the average of max of left side and min of right side
                else:
                    return (max(maxX, maxY) + min(minX, minY)) / 2
            elif maxX > minY:
                # Move towards the left in nums1
                high = partitionX - 1
            else:
                # Move towards the right in nums1
                low = partitionX + 1
        
        # If input arrays are not sorted or invalid inputs
        raise ValueError("Input arrays are not valid!")
