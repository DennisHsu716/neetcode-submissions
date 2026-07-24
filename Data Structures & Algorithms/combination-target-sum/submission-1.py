class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, path, current_sum):
            if current_sum > target:
                return 
            
            if current_sum == target:
                res.append(path[:])
                return 
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i, path, nums[i] + current_sum)
                path.pop()
            
        backtrack(0, [], 0)
        return res 
            