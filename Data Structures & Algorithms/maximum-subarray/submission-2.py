class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_num = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            max_num = max(nums[i], max_num + nums[i])
            res = max(res, max_num)
        return res 