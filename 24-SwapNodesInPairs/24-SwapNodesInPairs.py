# Last updated: 11/1/2025, 9:35:18 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy

        while head and head.next:
            temp = head.next
            head.next = temp.next
            temp.next = prev.next
            prev.next = temp
            prev = prev.next.next
            head = head.next

        return dummy.next     