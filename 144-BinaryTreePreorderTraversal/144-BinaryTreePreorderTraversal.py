# Last updated: 11/1/2025, 9:34:28 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        if root is not None:
            return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

        