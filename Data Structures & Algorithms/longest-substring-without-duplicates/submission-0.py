class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left = 0
        window = []
        for i in range(len(s)):
            while s[i] in window:
                window.remove(s[left])
                left += 1
            window.append(s[i])
            res = max(res, i - left + 1)
        return res

        # i in seen, seen.remove[l], l+= 1