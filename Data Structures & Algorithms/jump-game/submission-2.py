class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_step = 0 
        for start, end in enumerate(nums):
            if start > max_step:
                return False 
            
            max_step = max(max_step, start + end)
        return True