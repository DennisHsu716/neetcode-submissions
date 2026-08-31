class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        res = 0
        row = len(grid)
        col = len(grid[0])
        visited = set()

        def dfs(r, c):
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == 0 or (r, c) in visited:
                return 0
            
            visited.add((r, c))
            
            top = dfs(r + 1, c)
            botton = dfs(r - 1, c)
            left = dfs(r, c + 1)
            right = dfs(r, c - 1)
            
            return top + botton + left + right + 1

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = dfs(r, c)
                    res = max(res, max_area)
        return res 