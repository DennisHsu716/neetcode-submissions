"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clone = {}

        def dfs(node:Optional):
            if not node:
                return None
            
            if node in clone:
                return clone[node]
            
            newNode = Node(node.val)
            clone[node] = newNode

            for i in node.neighbors:
                cloneneighbors = dfs(i)
                newNode.neighbors.append(cloneneighbors)
            return newNode
        return dfs(node)