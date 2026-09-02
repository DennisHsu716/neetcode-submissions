class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        pre1 = nums[0]
        pre2 = max(nums[0], nums[1])

        for i in range(2, n):
            curr = max(nums[i] + pre1, pre2)
            pre1 = pre2
            pre2 = curr
        return pre2