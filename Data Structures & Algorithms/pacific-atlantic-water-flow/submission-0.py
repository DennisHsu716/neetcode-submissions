class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()
        row = len(heights)
        col = len(heights[0])
        
        def dfs(r, c, visited, preheigh):
            if r < 0 or r >= row or c < 0 or c >= col or (r, c) in visited:
                return 

            current = heights[r][c]    
            if current < preheigh:
                return 


            visited.add((r, c))

            dfs(r + 1, c, visited, current)
            dfs(r - 1, c, visited, current)
            dfs(r, c + 1, visited, current)
            dfs(r, c - 1, visited, current)


        for r in range(row):
            dfs(r, 0, pac, -1)
        
        for c in range(col):
            dfs(0, c, pac, -1)

        for r in range(row):
            dfs(r, col - 1, atl, -1)

        for c in range(col):
            dfs(row - 1, c, atl, -1)

        ans = []
        for r in range(row):
            for c in range(col):
                if (r, c) in pac and (r, c) in atl:
                    ans.append([r, c])
        return ans        