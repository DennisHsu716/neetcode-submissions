class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = []
        row = len(board)
        col = len(board[0])
        visited = set()

        def dfs(r, c, path):
            if path == len(word):
                return True 
            
            if r < 0 or r >= row or c < 0 or c >= col or (r, c) in visited:
                return False 
            
            if board[r][c] != word[path]:
                return False 
            
            visited.add((r, c))

            found = (
                dfs(r + 1, c, path + 1) or 
                dfs(r - 1, c, path + 1) or 
                dfs(r, c + 1, path + 1) or 
                dfs(r, c - 1, path + 1)
            )

            visited.remove((r, c))
            return found
        
        for r in range(row):
            for c in range(col):
                if dfs(r, c, 0):
                    return True 
        return False 