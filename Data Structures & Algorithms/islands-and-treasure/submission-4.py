class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        quene = deque()
        row = len(grid)
        col = len(grid[0])
        INF = 2147483647
        
        for r in range(row):    
            for c in range(col):
                if grid[r][c] == 0:
                    quene.append((r, c))

        while quene:
            r, c = quene.popleft()    
            if r + 1 < row and grid[r + 1][c] == INF:
                grid[r + 1][c] = grid[r][c] + 1
                quene.append((r + 1, c))

            if r - 1 >= 0 and grid[r - 1][c] == INF:
                grid[r - 1][c] = grid[r][c] + 1
                quene.append((r - 1, c))

            if c + 1 < col and grid[r][c + 1] == INF:
                grid[r][c + 1] = grid[r][c] + 1
                quene.append((r, c + 1))
            
            if c - 1 >= 0 and grid[r][c - 1] == INF:
                grid[r][c - 1] = grid[r][c] + 1
                quene.append((r, c - 1))
        