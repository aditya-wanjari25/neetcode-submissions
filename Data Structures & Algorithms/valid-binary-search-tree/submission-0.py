# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node, min_limit, max_limit):
            if node is  None:
                return True
            
            if node.val <= min_limit or node.val >= max_limit:
                return False
            
            left_side = validate(node.left, min_limit, node.val)            
            right_side = validate(node.right, node.val, max_limit)

            return left_side and right_side
        
        return validate(root, float('-inf'),float('inf'))
        

        