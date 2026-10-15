class Solution:
    def rob(self, nums: List[int]) -> int:
        pre1 = nums[0]
        pre2 = max(nums[0], nums[1])


        for i in range(2, len(nums)):
            curr = max(pre2, nums[i] + pre1)
            pre1 = pre2
            pre2 = curr
        return pre2