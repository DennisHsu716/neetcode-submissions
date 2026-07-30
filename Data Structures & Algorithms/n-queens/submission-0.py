class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols = set()
        diag1 = set()
        diag2 = set()
        board = [["."] * n for _ in range(n)]

        def backtrack(row):
            if row == n:
                solution = []

                for i in board:
                    solution.append("".join(i))
                res.append(solution)
                return 
                
            for col in range(n):
                if col in cols:
                    continue 
                
                if row - col in diag1:
                    continue
                
                if row + col in diag2:
                    continue             
                
                board[row][col] = "Q"

                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                backtrack(row + 1)

                board[row][col] = "."

                cols.remove(col)
                diag1.remove(row - col) 
                diag2.remove(row + col)
            
        backtrack(0)
        return res 
