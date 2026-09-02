class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        quene = deque()
        row = len(grid)
        col = len(grid[0])
        fresh = 0
        time = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    quene.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        
        while quene:
            size = len(quene)
            infect = False 
            while size:
                
                r, c = quene.popleft()
                if r + 1 < row and grid[r + 1][c] == 1:
                    grid[r + 1][c] = 2
                    fresh -= 1 
                    infect = True 
                    quene.append((r + 1, c))    
                
                if r - 1 >= 0 and grid[r - 1][c] == 1:
                    grid[r - 1][c] = 2
                    fresh -= 1
                    infect = True 
                    quene.append((r - 1, c))
                
                if c + 1 < col and grid[r][c + 1] == 1:
                    grid[r][c + 1] = 2
                    fresh -= 1
                    infect = True 
                    quene.append((r, c + 1))
                
                if c - 1 >= 0 and grid[r][c - 1] == 1:
                    grid[r][c - 1] = 2
                    fresh -= 1
                    infect = True 
                    quene.append((r, c - 1))
                size -= 1
            if infect:
                time += 1
        
        if fresh == 0:
            return time 
        else:
            return -1 
         