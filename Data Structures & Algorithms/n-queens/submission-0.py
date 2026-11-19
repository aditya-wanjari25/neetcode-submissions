class Solution:
    def isSafe(self, cols, row, col):
        for r in range(row):
            c = cols[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        cols = []

        def backtrack(row):
            if row == n:  # every row has a queen
                solutions.append(["." * c + "Q" + "." * (n - c - 1) for c in cols])
                return
            for col in range(n):
                if self.isSafe(cols, row, col):
                    cols.append(col)      # choose
                    backtrack(row + 1)    # explore
                    cols.pop()            # unchoose

        backtrack(0)
        return solutions