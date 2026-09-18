class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mini = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            mini = max(nums[i], nums[i] + mini)
            res = max(res, mini)
        return res 