class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = []

        for i in nums:
            if i in res:
                return True 
            else:
                res.append(i)
        return False 