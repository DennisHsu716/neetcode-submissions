class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = nums[0]
        curr_min = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            old_max = curr_max
            old_min = curr_min

            curr_max = max(nums[i], old_max * nums[i], old_min * nums[i])
            curr_min = min(nums[i], old_max * nums[i], old_min * nums[i])
            res = max(res, old_max)
        return res 