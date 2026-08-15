class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = nums[0]
        cur_min = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            old_max = cur_max 
            old_min = cur_min

            cur_max = max(nums[i], old_min * nums[i], old_max * nums[i])
            cur_min = max(nums[i], old_min * nums[i], old_max * nums[i])
            res = max(res, cur_max)
        return res 