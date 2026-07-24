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

                path.append(nums[i])
                used[i] = True
                backtrack(used, path)
                path.pop()
                used[i] = False 

        backtrack([False] * len(nums), [])
        return res 