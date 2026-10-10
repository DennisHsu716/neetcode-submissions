class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, path, curr):
            if curr > target:
                return 
            
            if curr == target:
                res.append(path[:])
                return 
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i, path, curr + nums[i])
                path.pop()
            
        backtrack(0, [], 0)
        return res 