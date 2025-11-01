# Last updated: 11/1/2025, 9:34:32 PM
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':    
        hash = {None:None}
        cur = head
        
        while cur:
            hash[cur] = Node(cur.val)
            cur = cur.next
            
        cur = head
        
        while cur:
            copy = hash[cur]
            copy.next = hash[cur.next]
            copy.random = hash[cur.random]
            cur = cur.next
            
        return hash[head]