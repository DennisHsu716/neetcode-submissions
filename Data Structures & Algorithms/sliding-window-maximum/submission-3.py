class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        left = 0
        for i in range(k - 1, len(nums)):
            window = nums[left: i + 1]
            res.append(max(window))
            left += 1
        return res 
