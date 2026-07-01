class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        res = 0

        for i in num:
            if i - 1 not in num:
                curr = i
                length = 1

                while curr + 1 in num:
                    curr += 1
                    length += 1
                res = max(res, length)
        return res 