class Solution:
    def jump(self, nums: List[int]) -> int:
        faster = 0
        jump = 0
        end = 0

        for i in range(len(nums) - 1):
            faster = max(faster, nums[i] + i)
            if i == end:
                end = faster
                jump += 1 
        return jump