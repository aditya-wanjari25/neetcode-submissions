class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # 1. This variable will keep track of our maximum diameter 
        self.max_diameter = 0
        
        # 2. A helper function to calculate depth
        def depth(node):
            if node is None:
                return 0
            
            # Find the depths of the left and right sides
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            
            # 3. The side calculation: update max_diameter if this path is longer!
            # (Notice we are adding the depths together, measuring edges)
            self.max_diameter = max(self.max_diameter, left_depth + right_depth)
            
            # 4. Return the depth to the parent (exactly what you did in maxDepth)
            return 1 + max(left_depth, right_depth)
        
        # Kick off the recursion from the root
        depth(root)
        
        # Return the largest diameter we found anywhere in the tree
        return self.max_diameter