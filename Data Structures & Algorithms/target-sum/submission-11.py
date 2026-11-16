class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if abs(target) > total:
            return 0
        
        sub_target = (total + target) // 2
        dp = [0] * (sub_target + 1)
        dp[0] = 1

        for num in nums:
            for i in range(sub_target, num - 1, -1):
                dp[i] += dp[i - num]
        return dp[sub_target]