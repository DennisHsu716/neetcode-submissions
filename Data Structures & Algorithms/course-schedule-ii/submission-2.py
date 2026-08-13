class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        for course, preq in prerequisites:
            graph[course].append(preq)
        state = [0] * numCourses
        res = []

        def dfs(course):
            if state[course] == 1:
                return False 
            
            if state[course] == 2:
                return True 
            
            state[course] = 1

            for i in graph[course]:
                if not dfs(i):
                    return False 
            
            state[course] = 2
            res.append(course)
            return True 
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res 