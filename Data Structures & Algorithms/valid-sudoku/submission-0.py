import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Skip empty cells
                if val == ".":
                    continue
                
                # 1. Define the unique key for the current 3x3 box
                box_key = (r // 3, c // 3)
                
                # 2. Check if the value already exists in the row, col, or box
                if (val in rows[r] or 
                    val in cols[c] or 
                    val in boxes[box_key]):
                    return False
                
                # 3. If it's valid, add it to our tracking sets
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_key].add(val)
                
        return True