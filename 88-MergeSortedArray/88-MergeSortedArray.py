# Last updated: 11/1/2025, 9:34:51 PM
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 1st way is to slice and sort
        # nums1[m:] = nums2
        # nums1.sort()

        # using two pointers and one right pointer 
        m1, n1, r = m - 1, n - 1, m + n - 1

        while m1 >= 0 and n1 >= 0:
            if nums1[m1] > nums2[n1]:
                nums1[r] = nums1[m1]
                m1 -= 1
            else:
                nums1[r] = nums2[n1]
                n1 -= 1
            r -= 1

        # If any nums2 elements left
        while n1 >= 0:
            nums1[r] = nums2[n1]
            r -= 1
            n1 -= 1
        