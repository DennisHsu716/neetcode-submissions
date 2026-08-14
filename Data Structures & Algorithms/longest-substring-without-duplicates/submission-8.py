class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left = 0
        window = set()

        for i in range(len(s)):
            while s[i] in window:
                window.remove(s[left])
                left += 1
            window.add(s[i])
            res = max(res, i - left + 1)
        return res 