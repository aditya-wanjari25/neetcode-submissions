# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root is None:
            return None
        
        # swap nodes
        root.left, root.right = root.right, root.left
        # invert left half
        self.invertTree(root.left)

        # invert right half
        self.invertTree(root.right)

        return root

        