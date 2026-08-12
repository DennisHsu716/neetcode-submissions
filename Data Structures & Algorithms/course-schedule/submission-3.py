class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]

        for course, preq in prerequisites:
            graph[preq].append(course)
        
        state = [0] * numCourses
        
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
            return True 

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True 
