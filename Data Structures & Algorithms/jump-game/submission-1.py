class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_step = 0
        for val, step in enumerate(nums):
            if val > max_step:
                return False 

            max_step = max(max_step, val + step) 
        return True 
