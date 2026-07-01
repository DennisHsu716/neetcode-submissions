class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = []
        for i in range(len(nums)):
            if nums[i] in res:
                return True 
            else:
                res.append(nums[i])
        return False