# Last updated: 11/1/2025, 9:34:44 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #implement in post order approach
        #or just do max of left and right childs:
        #if root empty return 0
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))