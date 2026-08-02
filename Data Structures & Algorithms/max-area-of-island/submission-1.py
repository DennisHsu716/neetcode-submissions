class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = set()
        maxArea = 0

        def dfs(r, c):
            if (r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == 0 or (r, c) in visited):
                return 0
            
            visited.add((r, c))

            left = dfs(r + 1, c)
            right = dfs(r - 1, c)
            top = dfs(r, c + 1)
            botton = dfs(r, c - 1)

            return left + right + top + botton + 1
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = dfs(r, c)
                    maxArea = max(maxArea, area)
        return maxArea
