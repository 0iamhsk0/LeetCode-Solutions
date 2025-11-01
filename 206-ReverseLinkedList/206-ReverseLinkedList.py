# Last updated: 11/1/2025, 9:34:09 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Using fast and slow pointers
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head  
        curr = head
        slow = None

        while curr is not None:
            fast = curr.next
            curr.next = slow
            slow = curr
            curr = fast
        
        return slow

# Similar Approach:
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head:
#             return head

#         node = None
#         while head:
#             temp = head.next
#             head.next = node
#             node = head
#             head = temp
#         return node