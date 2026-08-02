class TriesNode():
    def __init__(self):
        self.children = {}
        self.end = False 
        self.word = ""
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        self.root = TriesNode()

        for word in words:
            node = self.root 
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TriesNode()
                node = node.children[ch]
            node.end = True 
            node.word = word 
        
        row = len(board)
        col = len(board[0])

        def dfs(node, r, c):
            nonlocal res, row, col
            if r < 0 or r >= row or c < 0 or c >= col:
                return False 
            
            ch = board[r][c]

            if ch == "#":
                return False 
            
            if ch not in node.children:
                return False 
            node = node.children[ch]
            board[r][c] = "#"

            if node.end == True:
                res.append(node.word)
                node.end = False 
            
            dfs(node, r + 1, c)
            dfs(node, r - 1, c)
            dfs(node, r, c + 1)
            dfs(node, r, c - 1)

            board[r][c] = ch
        
        for r in range(row):
            for c in range(col):
                dfs(self.root, r, c)
        return res 