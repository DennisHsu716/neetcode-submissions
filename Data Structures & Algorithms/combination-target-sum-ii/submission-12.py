class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, path, curr):
            if curr > target:
                return 
            
            if curr == target:
                res.append(path[:])
                return 
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue 
                path.append(candidates[i])
                backtrack(i + 1, path, candidates[i] + curr)
                path.pop()
        
        backtrack(0, [], 0)
        return res 