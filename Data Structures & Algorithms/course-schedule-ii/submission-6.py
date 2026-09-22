class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        for course, preq in prerequisites:
            graph[preq].append(course)
        
        state = [0] * numCourses
        count = []

        def dfs(course):
            nonlocal count 

            if state[course] == 1:
                return False 

            if state[course] == 2:
                return True 
            
            state[course] = 1

            for i in graph[course]:
                if not dfs(i):
                    return False 
            
            state[course] = 2
            count.append(course)
            return True 
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        count.reverse()
        return count 
