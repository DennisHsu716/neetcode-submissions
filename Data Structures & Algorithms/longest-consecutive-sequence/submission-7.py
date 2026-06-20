class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #set()
        #if i - 1 not in count create
        num = set(nums)
        res = 0
        for i in num:
            if i - 1 not in num:
                count = i
                length = 1
            while count + 1 in num:
                count += 1
                length += 1
            res = max(res, length)
        return res