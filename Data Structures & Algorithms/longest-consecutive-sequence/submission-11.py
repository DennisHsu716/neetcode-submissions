class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        num = set(nums)

        for i in num:
            if i - 1 not in num:
                current = i
                length = 1 
                while current + 1 in num:
                    current += 1
                    length += 1
                res = max(res, length)
        return res 