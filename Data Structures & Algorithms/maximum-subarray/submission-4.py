class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxvalue = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            maxvalue = max(nums[i], maxvalue + nums[i])
            res = max(res, maxvalue)
        return res 
        