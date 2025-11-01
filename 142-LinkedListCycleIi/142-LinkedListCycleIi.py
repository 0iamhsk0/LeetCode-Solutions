# Last updated: 11/1/2025, 9:34:29 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Approach 1: Using HashSet, not space efficient
# class Solution:
#     def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         hash_set = set()
#         while head:
#             if head in hash_set:
#                 return head
#             hash_set.add(head)
#             head = head.next
      
#         return None

# Approach 2: Using Fast and Slow Pointers
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None 

        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow  
        
            