class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = {}

        for i in nums:
            res[i] = res.get(i, 0) + 1
        
        for i in nums:
            if res[i] == 1:
                return i