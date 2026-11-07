class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        curr = nums[0]

        for i in range(1, len(nums)):
            curr = max(nums[i], nums[i] + curr)
            res = max(curr, res)
        return res 
