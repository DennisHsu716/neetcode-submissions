class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        count = 0
        visited = set()
        
        def dfs(node):
            nonlocal count 
            visited.add(node)
            for i in graph[node]:
                if i in visited:
                    continue 
                dfs(i)

        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        return count 
        

            
