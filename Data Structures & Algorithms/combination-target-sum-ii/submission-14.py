class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(start, path, current):
            #if big
            if current > target:
                return 
            #same 
            if current == target:
                res.append(path[:])
                return 
            #start BT
            for i in range(start, len(candidates)):
                #skip if same 
                if i > start and candidates[i] == candidates[i - 1]:
                    continue 

                path.append(candidates[i])
                backtrack(i + 1, path, current + candidates[i])
                path.pop()
        
        backtrack(0, [], 0)
        return res 