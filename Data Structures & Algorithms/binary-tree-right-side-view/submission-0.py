from collections import deque
from typing import Optional, List

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        result = []
        queue = deque()
        queue.append(root)

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if i == (level_size - 1):
                    result.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            
        return result