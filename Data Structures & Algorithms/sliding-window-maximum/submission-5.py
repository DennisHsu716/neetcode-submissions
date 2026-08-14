class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dp = deque()
        left = 0
        res = []


        for i in range(len(nums)):
            while dp and nums[dp[-1]] <= nums[i]:
                dp.pop()
            
            dp.append(i)
            
            if dp[0] < left:
                dp.popleft()
            
            if i >= k - 1:
                res.append(nums[dp[0]])
                left += 1

        return res 