class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])

        dp = [[0] * col for _ in range(row)]

        def dfs(r, c):
            if dp[r][c] != 0:
                return dp[r][c]
            
            dp[r][c] = 1

            if r - 1 >= 0 and matrix[r - 1][c] > matrix[r][c]:
                dp[r][c] = max(dp[r][c], 1 + dfs(r - 1, c))
            
            if r + 1 < row and matrix[r + 1][c] > matrix[r][c]:
                dp[r][c] = max(dp[r][c], 1 + dfs(r + 1, c))
            
            if c - 1 >= 0 and matrix[r][c - 1] > matrix[r][c]:
                dp[r][c] = max(dp[r][c], 1 + dfs(r, c - 1))
            
            if c + 1 < col and matrix[r][c + 1] > matrix[r][c]:
                dp[r][c] = max(dp[r][c], 1 + dfs(r, c + 1))

            return dp[r][c]
        
        res = 0
        for r in range(row):
            for c in range(col):
                res = max(res, dfs(r, c))
        return res 
