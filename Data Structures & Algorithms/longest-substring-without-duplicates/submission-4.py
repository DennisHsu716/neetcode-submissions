class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        window = []
        res = 0

        for i in range(len(s)):
            while s[i] in window:
                window.remove(s[left])
                left += 1
            window.append(s[i])
            res = max(res, i - left + 1)
        return res 
