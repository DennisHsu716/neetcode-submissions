class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        seen = set()

        def dfs(r, c, index):
            if index == len(word):
                return True 
                
            if r < 0 or r >= row or c < 0 or c >= col or (r, c) in seen:
                return False 
            
            if board[r][c] != word[index]:
                return False 
            
            seen.add((r, c))

            found = (
                dfs(r + 1, c, index + 1) or 
                dfs(r - 1, c, index + 1) or 
                dfs(r, c + 1, index + 1) or 
                dfs(r, c - 1, index + 1)
            )

            seen.remove((r, c))
            return found 
        
        for r in range(row):
            for c in range(col):
                if dfs(r, c, 0):
                    return True 
        return False 