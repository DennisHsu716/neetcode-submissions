class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        seen = set()
        island = 0

        def dfs(r, c):
            if r < 0 or r >= row or c < 0 or c >= col or (r, c) in seen or grid[r][c] == "0":
                return 
            
            seen.add((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for r in range(row):
            for c in range(col):
                if (r, c) not in seen and grid[r][c] == "1":
                    dfs(r, c)
                    island += 1
        return island 
