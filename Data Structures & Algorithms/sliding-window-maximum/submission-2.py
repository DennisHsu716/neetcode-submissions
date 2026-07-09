class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        res = [] 
        window = {}

        for i in range(k - 1, len(nums)):
            window = nums[left:i+1]
            res.append(max(window))
            left+= 1
        return res 