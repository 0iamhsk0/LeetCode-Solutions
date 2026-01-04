# Last updated: 1/4/2026, 1:04:07 PM
1class Solution:
2    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
3        """
4        Do not return anything, modify nums1 in-place instead.
5        """
6        # Latest sol
7        m1, n1, p = m - 1, n - 1, m + n - 1
8
9        while m1 >= 0 and n1 >= 0:
10            if nums1[m1] < nums2[n1]:
11                nums1[p] = nums2[n1]
12                p -= 1
13                n1 -= 1
14            else:
15                nums1[p] = nums1[m1]
16                nums1[m1] = nums2[n1]
17                p -= 1
18                m1 -= 1
19
20        while n1 >= 0:
21            nums1[p] = nums2[n1]
22            p -= 1
23            n1 -= 1
24
25        return nums1
26
27
28
29
30        # # 1st way is to slice and sort
31        # # nums1[m:] = nums2
32        # # nums1.sort()
33
34        # # using two pointers and one right pointer 
35        # m1, n1, r = m - 1, n - 1, m + n - 1
36
37        # while m1 >= 0 and n1 >= 0:
38        #     if nums1[m1] > nums2[n1]:
39        #         nums1[r] = nums1[m1]
40        #         m1 -= 1
41        #     else:
42        #         nums1[r] = nums2[n1]
43        #         n1 -= 1
44        #     r -= 1
45
46        # # If any nums2 elements left
47        # while n1 >= 0:
48        #     nums1[r] = nums2[n1]
49        #     r -= 1
50        #     n1 -= 1
51        