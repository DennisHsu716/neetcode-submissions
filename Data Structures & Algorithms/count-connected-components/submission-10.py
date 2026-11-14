class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = set()
        count = 0

        def dfs(node):
            nonlocal count
            seen.add(node)
            for i in graph[node]:
                if i in seen:
                    continue 
                dfs(i)
        
        for i in range(n):
            if i not in seen:
                count += 1
                dfs(i)
        return count
