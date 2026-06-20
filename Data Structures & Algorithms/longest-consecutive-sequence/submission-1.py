class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)

        for i in range(len(nums)):
            if i - 1 not in num:
                current = i
                length = 1
                while current + 1 in num:
                    length += 1
                    current += 1
        return length 