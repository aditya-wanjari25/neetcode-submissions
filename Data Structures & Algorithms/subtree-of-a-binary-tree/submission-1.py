# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        
        if root is None:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
        
        left_side = self.isSubtree(root.left, subRoot)
        right_side = self.isSubtree(root.right, subRoot)

        return left_side or right_side
    
    def isSameTree(self,root, subRoot):
        if root is None and subRoot is None:
            return True
        
        if root is None or subRoot is None:
            return False
        
        if root.val != subRoot.val:
            return False
        
        left_side = self.isSameTree(root.left, subRoot.left)
        right_side = self.isSameTree(root.right, subRoot.right)

        return left_side and right_side



        