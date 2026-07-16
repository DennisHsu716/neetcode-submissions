class TriesNode:
    def __init__(self):
        self.children = {}
        self.end = False 

class PrefixTree:

    def __init__(self):
        self.root = TriesNode()
        

    def insert(self, word: str) -> None:
        node = self.root

        for i in word:
            if i not in node.children:
                node.children[i] = TriesNode()
            node = node.children[i]
        node.end = True 


    def search(self, word: str) -> bool:
        node = self.root

        for i in word:
            if i not in node.children:
                return False 
            node = node.children[i]
        return node.end 
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for i in prefix:
            if i not in node.children:
                return False 
            node = node.children[i]
        return True
        
        