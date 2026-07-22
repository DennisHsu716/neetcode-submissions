class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_nums = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            max_nums = max(nums[i], nums[i] + max_nums)
            res = max(res, max_nums)
        return res 