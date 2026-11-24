class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def backtrack(r, c, i):
            # Base case: success
            if i == len(word):
                return True

            # Base cases: failure (pruning)
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return False
            if board[r][c] != word[i]:
                return False

            # Choose: mark this cell as used
            temp = board[r][c]
            board[r][c] = "#"

            # Explore: try all 4 neighbors for the next letter
            found = (backtrack(r + 1, c, i + 1) or
                     backtrack(r - 1, c, i + 1) or
                     backtrack(r, c + 1, i + 1) or
                     backtrack(r, c - 1, i + 1))

            # Unchoose: restore the cell
            board[r][c] = temp

            return found

        # Outer loop: try every cell as a starting point
        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r, c, 0):
                    return True
        return False