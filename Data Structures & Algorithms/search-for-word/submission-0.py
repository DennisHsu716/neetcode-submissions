class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        res = set()

        def backtrack(i, j, index):
            if index == len(word):
                return True 
            
            if i < 0 or i >= row or j < 0 or j >= col:
                return False 
            
            if (i, j) in res:
                return False 
            
            if board[i][j] != word[index]:
                return False 
            
            res.add((i, j))

            found = (
                backtrack(i - 1, j, index + 1) or
                backtrack(i, j - 1, index + 1) or 
                backtrack(i + 1, j, index + 1) or 
                backtrack(i, j + 1, index + 1)
            )

            res.remove((i, j))
            return found
        
        for i in range(row):
            for j in range(col):
                if backtrack(i, j, 0):
                    return True 
        return False 
