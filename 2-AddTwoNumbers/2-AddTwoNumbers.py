# Last updated: 11/1/2025, 9:35:32 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        ptr = result

        add = 0
        carry = 0

        while l1 != None or l2 != None:
            add = 0 + carry
            if l1 != None:
                add += l1.val
                l1 = l1.next
            if l2 != None:
                add += l2.val
                l2 = l2.next
            carry = add // 10
            add = add % 10
            ptr.next = ListNode(add)
            ptr = ptr.next
        
        if carry == 1:
            ptr.next = ListNode(1)
        
        return result.next

