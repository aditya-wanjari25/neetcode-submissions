# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0

        def findGoodNodes(node, max_so_far):
            if node is None:
                return 0

            if node.val >= max_so_far:
                score = 1
            else:
                score = 0
            
            new_max = max(node.val, max_so_far)
            left_side = findGoodNodes(node.left, new_max)
            right_side = findGoodNodes(node.right, new_max)

            
            return left_side + right_side + score
        
        return findGoodNodes(root, root.val)
         
            



        
        
