class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        window = {}
        max_freq = 0
        res = 0

        for i in range(len(s)):
            window[s[i]] = window.get(s[i], 0) + 1
            max_freq = max(max_freq, window[s[i]])

            while (i - left + 1) - max_freq > k:
                 window[s[left]] -= 1
                 left += 1

            res = max(res, i - left + 1)
        return res 