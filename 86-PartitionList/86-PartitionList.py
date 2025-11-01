# Last updated: 11/1/2025, 9:34:53 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None

        before_head = ListNode(0)
        before = before_head
        after_head = ListNode(0)
        after = after_head

        # Seperating into 2 lists
        current = head
        while current is not None:
            if current.val < x:
                before.next = current
                before = before.next
            else:
                after.next = current
                after = after.next
            current = current.next

        # Joining them again
        after.next = None
        before.next = after_head.next

        return before_head.next


            
