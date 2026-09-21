class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        island = 0
        maxArea = 0
        res = set()

        def dfs(r, c):
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == 0 or (r, c) in res:
                return 0
            
            res.add((r, c))

            top = dfs(r + 1, c)
            botton = dfs(r - 1, c)
            left = dfs(r, c + 1)
            right = dfs(r, c - 1)

            return top + botton + left + right + 1
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r, c) not in res:
                    island = dfs(r, c)
                    maxArea = max(maxArea, island)
        return maxArea
