# Last updated: 11/1/2025, 9:34:48 PM
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # standard BST code
        # if not root:
        #     return []
        # if root is not None:
        #     return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        ## Morris traversal(inorder traversal with a roundabout arpproach):
        inorder = []
        curr = root
        #1st case: (if left is none, append the curr value), everything in a loop till curr is not none
        while curr is not None:
            if not curr.left:
                inorder.append(curr.val)
                curr = curr.right
            #2nd case: else traverse till the rightmost of left subrtree and make threads to reach back to the root:
            else:
                next = curr.left
                #traverse till the rightmost node in Left tree
                while next.right is not None and next.right != curr:
                    next = next.right
                if next.right is None:
                    next.right = curr
                    curr = curr.left
                else:
                    next.right = None
                    inorder.append(curr.val)
                    curr = curr.right
        return inorder




        

            
        
        