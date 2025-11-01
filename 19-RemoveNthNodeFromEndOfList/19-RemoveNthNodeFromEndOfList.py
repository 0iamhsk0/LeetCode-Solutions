# Last updated: 11/1/2025, 9:35:20 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None

        # length of list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        # If n equals length, remove the head node
        if n == length:
            head = head.next
            return head

        # move to the (length-n)th node
        current = head
        for _ in range(length - n - 1):
            current = current.next

        # Delete the nth node from the end
        if current.next:
            current.next = current.next.next

        return head
