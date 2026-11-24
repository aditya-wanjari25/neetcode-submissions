class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def backtrack(i, r, c):        # Step 1: what parameters?
            # Step 2: base cases
            if i == len(word):
                return True
            
            if r < 0 or r>= ROWS or c < 0 or c >= COLS:
                return False
            
            if board[r][c] != word[i]:
                return False
                        
            # Step 4: mark this cell as used
            temp = board[r][c]
            board[r][c] = "#"

            
            # Step 3: explore neighbors
            found = (
                backtrack(i+1, r+1, c) or
                backtrack(i+1, r-1, c) or
                backtrack(i+1, r, c+1) or
                backtrack(i+1, r, c-1)
            )

            
            # Step 4: undo the mark
            board[r][c] = temp
            
            # return the result
            return found

        # Step 5: outer loop
        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(0,r,c):
                    return True
        
        return False










