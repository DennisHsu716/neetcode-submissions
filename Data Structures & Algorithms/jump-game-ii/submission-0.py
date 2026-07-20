class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = 0
        faster = 0
        end = 0
        for i in range(len(nums) - 1):
            faster = max(faster, nums[i] + i)
            if i == end:
                jump += 1
                end = faster
        return jump

                