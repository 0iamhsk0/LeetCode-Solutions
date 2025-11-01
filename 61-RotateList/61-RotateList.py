# Last updated: 11/1/2025, 9:35:01 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1st Approach: Breaking circular list
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        # finding length of the list
        len = 1
        last = head
        while last.next:
            last = last.next
            len += 1
        
        # making circular
        last.next = head

        k = k % len
        if k == 0:
            last.next = None
            return head

        skip = len - k
        new_tail = head
        for _ in range(skip - 1):
            new_tail = new_tail.next
        
        # break the circle
        new_head = new_tail.next
        new_tail.next = None
            
        return new_head
        
# 2nd approach: Slow and Fast pointer
# class Solution:
#     def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         if not head or not head.next or k == 0:
#             return head
        
#         length = 1
#         tail = head
#         while tail.next:
#             tail = tail.next
#             length += 1
        
#         k = k % length
#         if k == 0:
#             return head
        
#         slow = head
#         fast = head
#         for _ in range(k):
#             fast = fast.next
        
#         while fast.next:
#             slow = slow.next
#             fast = fast.next
        
#         new_head = slow.next
#         slow.next = None
#         fast.next = head
        
#         return new_head


        
        

        