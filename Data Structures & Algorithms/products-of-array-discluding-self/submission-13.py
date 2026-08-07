class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            produce = 1 
            for j in range(i + 1, len(nums)):
                if i == j:
                    continue 
                produce *= nums[j]
            res.append(produce)
        return res 
    