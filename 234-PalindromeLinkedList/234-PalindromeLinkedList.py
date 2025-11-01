# Last updated: 11/1/2025, 9:34:00 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# approach 1: using List
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:

#         # copy elements into array
#         dup = []
#         while head:
#             dup.append(head.val)
#             head = head.next
        
#         left, right = 0, len(dup) - 1
#         while left < right and dup[left] == dup[right]:
#             left += 1
#             right -= 1
#         return left >= right

# approach 2: slow and fast
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        rev = self.reverse(slow)
        while rev:
            if head.val != rev.val:
                return False
            head = head.next
            rev = rev.next
        
        return True

    def reverse(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

# Same but reduced code:
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         slow = head
#         fast = head

#         while fast and fast.next:
#             fast = fast.next.next
#             slow = slow.next

#         node = None
#         while slow:
#             temp = slow.next
#             slow.next = node
#             node = slow
#             slow = temp
        
#         first, second = head, node

#         while second:
#             if first.val != second.val:
#                 return False
            
#             first = first.next
#             second = second.next
        
#         return True
