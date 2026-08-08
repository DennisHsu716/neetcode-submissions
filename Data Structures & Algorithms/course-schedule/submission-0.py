class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        state = [0] * numCourses
        visited = set()

        #0 not yet
        #1 in visting 
        #2 done 

        def dfs(course):
            if state[course] == 1:
                return False 
            
            if state[course] == 2:
                return True 
            
            state[course] = 1
            
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False 
                
            state[course] = 2
            return True 
        return dfs(1)