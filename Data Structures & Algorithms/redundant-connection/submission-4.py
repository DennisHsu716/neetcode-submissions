class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = [[] for _ in range(n + 1)]

        def dfs(node, target):
            visited.add(node)
            if node == target:
                return True 
            
            for i in graph[node]:
                if i not in visited:
                    if dfs(i, target):
                        return True 
            return False 
        
        for a, b in edges:
            visited = set()

            if dfs(a, b):
                return [a, b]
            graph[a].append(b)
            graph[b].append(a)

            
