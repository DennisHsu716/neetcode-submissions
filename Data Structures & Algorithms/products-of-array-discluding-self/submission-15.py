class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        

        for i in range(len(nums)): 
            produce = 1 
            for j in range(len(nums)):
                if i == j:
                    continue 
                produce *= nums[j]
            res[i] = produce
        return res 
    