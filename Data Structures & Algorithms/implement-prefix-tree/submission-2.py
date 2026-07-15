class TriesNode:
    def __init__(self):
        self.children = {}
        self.is_end = False 

class PrefixTree:

    def __init__(self):
        self.root = TriesNode()

        

    def insert(self, word: str) -> None:
        node = self.root

        for i in word:
            if i not in node.children:
                node.children[i] = TriesNode()
            node = node.children[i]
        node.is_end = True 

    def search(self, word: str) -> bool:
        node = self.root

        for i in word:
            if i not in node.children:
                return False 
            node = node.children[i]
        return node.is_end
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for i in prefix:
            if i not in node.children:
                return False 
            node = node.children[i]
        return True 
        
        