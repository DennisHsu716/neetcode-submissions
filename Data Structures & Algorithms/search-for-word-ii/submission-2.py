class TriesNode:
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
        
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(node:TriesNode, row, col):
            nonlocal res, ROWS, COLS
            if row < 0 or row >= ROWS or col < 0 or col >= COLS:
                return False 
            
            ch = board[row][col]

            if ch == "#":
                return False 
            
            if ch not in node.children:
                return False 
            
            node = node.children[ch]
            board[row][col] = "#"

            if node.end == True:
                res.append(node.word)
                node.end = False 
            
            dfs(node, row + 1, col)
            dfs(node, row - 1, col)
            dfs(node, row, col + 1)
            dfs(node, row, col - 1)

            board[row][col] = ch
        
        for i in range(ROWS):
            for j in range(COLS):
                dfs(self.root, i, j)
        return res 
        