class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False  
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        
        def dfs(node, parent):
            visited.add(node)
            for i in graph[node]:
                if i == parent:
                    continue 
                if i in visited:
                    return False 
                if not dfs(i, node):
                    return False 
            return True 
        
        if not dfs(0, -1):
            return False 
        
        if len(visited) != n:
            return False 
        return True 
                

