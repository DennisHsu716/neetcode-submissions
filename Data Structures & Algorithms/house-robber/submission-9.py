class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        pre1 = nums[0]
        pre2 = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            curr = max(pre1 + nums[i], pre2)
            pre1 = pre2
            pre2 = curr
        return pre2