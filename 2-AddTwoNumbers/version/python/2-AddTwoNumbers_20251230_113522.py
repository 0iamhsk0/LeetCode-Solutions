# Last updated: 12/30/2025, 11:35:22 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
8        result = ListNode(0)
9        ptr = result
10        add = 0
11        carry = 0
12        while l1 != None or l2 != None:
13            add = 0 + carry
14            if l1 != None:
15                add += l1.val
16                l1 = l1.next
17            if l2 != None:
18                add += l2.val
19                l2 = l2.next
20            carry = add // 10
21            add = add % 10
22            ptr.next = ListNode(add)
23            ptr = ptr.next
24        
25        if carry == 1:
26            ptr.next = ListNode(1)
27        
28        return result.next
29
30