class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        island = 0
        maxArea = 0
        row = len(grid)
        col = len(grid[0])
        visited = set()


        def dfs(r, c):
            if r < 0 or r >= row or c < 0 or c >= col or (r, c) in visited or grid[r][c] == 0:
                return 0
            visited.add((r, c))
            top = dfs(r + 1, c)
            botton = dfs(r - 1, c)
            left = dfs(r, c + 1)
            right = dfs(r, c - 1)

            return top + botton + left + right + 1
        
        for r in range(row):
            for c in range(col):
                if (r, c) not in visited and grid[r][c] == 1:
                    island = dfs(r, c)
                    maxArea = max(maxArea, island)
        return maxArea