class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, path, current):
            if current > target:
                return
            if current == target:
                res.append(path[:])
                return 

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i, path, current + nums[i])
                path.pop()
        backtrack(0, [], 0)
        return res 