class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0

        for i in nums:
            if i - 1 not in nums:
                current = i
                length = 1
                while current + 1 in nums:
                    current += 1
                    length += 1
                res = max(res, length) 
        return res 