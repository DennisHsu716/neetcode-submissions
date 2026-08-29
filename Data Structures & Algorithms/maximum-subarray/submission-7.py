class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        curr_sum = nums[0]

        for i in range(1, len(nums)):
            curr_sum = max(nums[i], nums[i] + curr_sum)
            res = max(res, curr_sum)
        return res 