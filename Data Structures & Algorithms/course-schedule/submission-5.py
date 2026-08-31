class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for course, preq in prerequisites:
            graph[course].append(preq)
        
        state = [0] * numCourses

        def dfs(courses):
            if state[courses] == 1:
                return False 
            
            if state[courses] == 2:
                return True 
            
            state[courses] = 1

            for i in graph[courses]:
                if not dfs(i):
                    return False 
            
            state[courses] = 2
            return True 
        
        for course in range(numCourses):
            if not dfs(course):
                return False 

        return True  

            