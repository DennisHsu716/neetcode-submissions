class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            if len(nums) == 1:
                return nums[0]
            
            pre1 = nums[0]
            pre2 = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                curr = max(nums[i] + pre1, pre2)
                pre1 = pre2
                pre2 = curr
            return pre2
        
        if len(nums) == 1:
            return nums[0]
        
        return max(helper(nums[1:]), helper(nums[:-1]))