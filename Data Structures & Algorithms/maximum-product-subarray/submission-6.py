class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_min = nums[0]
        curr_max = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            old_min = curr_min
            old_max = curr_max

            curr_min = min(nums[i], nums[i] * old_min, nums[i] * old_max)
            curr_max = max(nums[i], nums[i] * old_min, nums[i] * old_max)

            res = max(res, curr_max)
        return res 