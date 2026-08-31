class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(used, path):
            if len(path) == len(nums):
                res.append(path[:])
                return 
            
            for i in range(len(nums)):
                if used[i]:
                    continue 
                used[i] = True
                path.append(nums[i])
                backtrack(used, path)
                path.pop()
                used[i] = False 
        
        backtrack([False] * len(nums), [])
        return res 
