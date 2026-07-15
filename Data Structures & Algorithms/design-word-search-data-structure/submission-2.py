class TriesNode:
    def __init__(self):
        self.children = {}
        self.end = False 

class WordDictionary:

    def __init__(self):
        self.root = TriesNode()
        

    def addWord(self, word: str) -> None:
        node = self.root

        for i in word:
            if i not in node.children:
                node.children[i] = TriesNode()
            node = node.children[i]
        node.end = True  
        

    def search(self, word: str) -> bool:
        def dfs(node:Optional[TreeNode], index):
            if index == len(word):
                return node.end 
            
            ch = word[index]

            if ch == ".":
                for i in node.children.values():
                    if dfs(i, index + 1):
                        return True
                return False 
            
            if ch not in node.children:
                return False 
            return dfs(node.children[ch], index + 1)
        return dfs(self.root, 0)
