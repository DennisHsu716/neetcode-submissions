class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = []
        for i in range(len(nums)):
            if nums[i] not in res:
                res.append(nums[i])
            else:
                return True 
        return False