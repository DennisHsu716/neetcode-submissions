class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = 0 
        faster = 0
        end = 0

        for i in range(len(nums) - 1):
            #find the farest one 
            faster = max(faster, i + nums[i])
            #if i == end need to restart
            if i == end:
                jump += 1
                end = faster
        return jump