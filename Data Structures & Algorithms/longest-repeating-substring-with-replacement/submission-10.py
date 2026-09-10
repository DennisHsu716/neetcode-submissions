class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        res = 0
        left = 0
        max_freq = 0

        for i in range(len(s)):
            window[s[i]] = window.get(s[i], 0) + 1
            max_freq = max(max_freq, window[s[i]])

            if (i - left + 1) - max_freq > k:
                window[s[left]] -= 1
                left += 1
            
            res = max(res, i - left + 1)
        return res 