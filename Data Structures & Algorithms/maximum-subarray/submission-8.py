class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_curr = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            max_curr = max(nums[i], nums[i] + max_curr)
            res = max(res, max_curr)
        return res 
