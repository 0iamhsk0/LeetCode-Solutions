# Last updated: 11/1/2025, 9:35:16 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or head.next is None:
            return head

        # Finding the length
        cnt = 0
        ptr = head
        while ptr:
            ptr = ptr.next
            cnt += 1
        
        # case when k > cnt
        if k > cnt:
            return head

        prev = None
        curr = head
        for _ in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        head.next = self.reverseKGroup(curr, k)
        return prev


        