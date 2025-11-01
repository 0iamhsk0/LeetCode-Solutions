# Last updated: 11/1/2025, 9:34:46 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #base case
        temp1 = []
        if not root:
            return temp1

        #using deque to implement
        q = collections.deque()
        q.append(root)

        while q:
            n = len(q)
            temp2 = []*n

            for _ in range(n):
                node = q.popleft()
                temp2.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            #return the leveled list
            temp1.append(temp2)
        return temp1


