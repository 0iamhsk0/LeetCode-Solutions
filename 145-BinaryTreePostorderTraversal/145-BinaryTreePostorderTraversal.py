# Last updated: 11/1/2025, 9:34:27 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        if root is not None:
            return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
        