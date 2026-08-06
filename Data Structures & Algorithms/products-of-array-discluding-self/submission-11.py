class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            produce = 1 
            for j in range(len(nums)):
                if i == j:
                    continue 
                produce *= nums[j]
            res.append(produce)
        return res 
    
#用暴力解法 把i定住,然後重複跑j,所以把其他不是i的值都乘起來