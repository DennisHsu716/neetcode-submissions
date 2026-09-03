class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        col = len(matrix[0])
        rows = set()
        cols = set()

        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    rows.add(r)
                    cols.add(c)

        for r in range(row):
            for c in range(col):
                if r in rows or c in cols:
                    matrix[r][c] = 0        
