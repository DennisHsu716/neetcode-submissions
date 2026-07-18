class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_step = 0

        for i, num in enumerate(nums):
            if i > max_step:
                return False 
            
            max_step = max(max_step, i + num)
        return True 